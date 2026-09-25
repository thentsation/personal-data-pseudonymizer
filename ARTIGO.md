🇧🇷 Português | [🇺🇸 English](ARTIGO.en-us.md)

# Transformando um script de exercício SOLID numa CLI de verdade

Esse projeto nasceu como um exercício de arquitetura: pegar um problema pequeno — mascarar PII em texto — e estruturá-lo em camadas seguindo SOLID. Fazia bem esse trabalho. O que faltava era tudo o que separa "código organizado" de "coisa que eu publicaria e confiaria": zero testes, zero tipagem, nenhuma forma de rodar sem editar o `main.py`, e nenhum CI vigiando nada disso.

## O que eu tinha em mãos

Um pacote `pseudonymizer/` com responsabilidades bem separadas — `NamedEntityDetector` (spaCy, PERSON/GPE), `PhoneDetector` e `EmailDetector` (regex), `TextProcessor` orquestrando os três e `PseudonymizerService` como fachada — mais um `main.py` na raiz que só imprimia um texto de exemplo fixo. Sem `__init__` de pacote, sem type hints, um único teste de integração (`test_pseudonymizer.py`) que checava se três substrings desapareciam do resultado, e um `config/requeriments.txt` (com erro de digitação) contendo só `spacy`, sem versão pinada.

Funcionava. Mas "funciona na minha máquina, para o meu texto de exemplo" não é uma CLI, é uma demo.

## Dar uma interface a quem só tinha um exemplo fixo

A primeira decisão foi parar de fingir que "rodar o projeto" significava "editar o código-fonte para trocar o texto". `src/main.py` ganhou um parser de argumentos de verdade com três formas de uso — texto como argumento posicional, texto via stdin (para compor com pipes), ou `--sample` para reproduzir o exemplo original sem precisar decorar a frase:

```python
def resolve_input_text(args: argparse.Namespace) -> str:
    if args.sample:
        return SAMPLE_TEXT
    if args.text is not None:
        return args.text
    return sys.stdin.read()
```

É uma CLI pequena, mas agora é uma CLI — `echo "John Doe lives in Paris" | python src/main.py` funciona, e o Dockerfile usa exatamente esse contrato (`ENTRYPOINT ["python", "src/main.py"]`, `CMD ["--sample"]` como default).

## Rede de proteção antes de qualquer coisa nova

Segui a mesma regra que aplico em qualquer produtização: nada de feature nova sem teste embaixo. O único teste antigo testava o sistema inteiro de ponta a ponta; separei a cobertura por responsabilidade — `test_email_detector.py` e `test_phone_detector.py` testam os regexes isoladamente (inclusive o caso de "não encontrou nada"), `test_entity_detector.py` verifica a extração de entidades e que o modelo do spaCy é cacheado entre instâncias (carregar `en_core_web_sm` do disco não é grátis), `test_text_processor.py` e `test_pseudonymizer_service.py` cobrem a orquestração, e `test_main.py` testa a CLI (resolução de input, stdin, `--sample`) sem depender de subprocess.

O resultado: 94% de cobertura de linha, sem mockar o spaCy — o modelo é pequeno (`en_core_web_sm`) e determinístico o suficiente para valer testar contra o modelo real em vez de um double.

Type hints em tudo (`disallow_untyped_defs = true` no mypy) obrigaram a nomear os tipos que estavam implícitos — por exemplo, `NamedEntity = tuple[int, int, str]` em vez de tuplas anônimas espalhadas pelo código.

## Cache de modelo: um detalhe que quase passou batido

`NamedEntityDetector.__init__` fazia `spacy.load("en_core_web_sm")` a cada instância. Numa CLI que roda uma vez e morre isso não importa, mas nos testes — que criam múltiplas instâncias — cada `spacy.load` custa dezenas de milissegundos. Um cache de módulo simples resolve para os dois casos:

```python
_MODEL_CACHE: dict[str, Language] = {}

def _load_model(model_name: str) -> Language:
    if model_name not in _MODEL_CACHE:
        _MODEL_CACHE[model_name] = spacy.load(model_name)
    return _MODEL_CACHE[model_name]
```

## Empacotamento: baixar o modelo faz parte do build, não do runtime

O Dockerfile é multi-stage (`python:3.12-slim`), roda como usuário não-root, e — ponto que copiei da lição aprendida nos outros projetos da mesma família (a API de sentimento pré-baixa o léxico do VADER no build por exatamente o mesmo motivo) — baixa o modelo do spaCy **durante o build da imagem**, não no primeiro request:

```dockerfile
RUN python -m spacy download en_core_web_sm
```

Sem isso, o primeiro `docker run` em qualquer lugar dependeria de rede disponível em runtime.

## CI, dependabot e release, para não depender de eu lembrar

O pipeline (`pipeline_python.yaml`) roda ruff (lint + format check), pytest com piso de cobertura de 90%, mypy e pip-audit — em toda PR, todo push e uma vez por dia agendado. O pipeline Docker builda, escaneia com Trivy e publica no GHCR quando o CI de Python passa na `main`. Dependabot cobre pip, a imagem base do Docker e as próprias GitHub Actions, com patch/minor mesclados automaticamente e major etiquetado para revisão manual num dashboard de issue que se atualiza (e se fecha) sozinho. Releases seguem semver automaticamente via Conventional Commits, a partir daqui em `v1.0.0`.

## O que ficou de fora, por ora

Não adicionei um `deploy.yaml` automático em push — diferente da API de sentimento e do chatbot, essa CLI não é um serviço de longa duração que precise ficar no ar; o workflow de deploy existe como `workflow_dispatch` manual, só para rodar a imagem publicada contra o texto de exemplo como smoke test, sem tocar em infraestrutura de produção sem eu pedir explicitamente.
