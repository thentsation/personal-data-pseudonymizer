# Personal Data Pseudonymizer

> Read in [English](README.md).

Uma CLI Python pequena que usa o spaCy para identificar entidades nomeadas em textos em inglês e substituí-las por pseudônimos (asteriscos), junto com números de telefone e endereços de e-mail. O objetivo é proteger informações pessoais identificáveis (PII) antes que o texto seja compartilhado, logado ou analisado.

Um artigo detalhado sobre o design e a produtização deste projeto está disponível em [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Funcionalidades

- Detecta **pessoas (PERSON)** e **localidades (GPE)** com o reconhecimento de entidades nomeadas do spaCy.
- Detecta números de telefone e e-mails com expressões regulares.
- Substitui cada ocorrência por asteriscos do mesmo tamanho, preservando o layout original do texto.
- Disponível como CLI (`src/main.py`) e como biblioteca reutilizável (`PseudonymizerService`).

### Exemplo de saída

```text
Original text:
The applicant John Doe, living at Maple Street, has the phone number +1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York.

Pseudonymized text:
The applicant **** ** ***, living at ***** Street, has the phone number ************, and his email is ********@*****.***. He also visited ***** York.
```

## Como rodar

```bash
make install       # cria o .venv, instala deps e o modelo do spaCy
make run           # roda a CLI contra o texto de exemplo embutido
echo "John Doe lives in Paris" | make run  # ou: .venv/bin/python src/main.py
```

Rodando com Docker:

```bash
make docker-build
make docker-run
```

## Desenvolvimento

```bash
make test        # pytest
make coverage     # pytest com relatório de cobertura
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI e deploy rodam no Jenkins da plataforma (`Jenkinsfile` → `appPipeline` da Shared Library `platform`, repo devops-platform), disparados por webhooks. Sem GitHub Actions.

- **PRs e branches** — validação do contrato; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` com cobertura ≥90% em Python 3.11 e 3.12, versões das ferramentas no `config/requirements-dev.txt`); `pip-audit` no `config/requirements.lock`; Trivy (CRITICAL/HIGH) na imagem de runtime.
- **main** — tudo acima e depois build e uma execução de teste da imagem (o job precisa terminar com exit 0; nada fica no ar), release com o python-semantic-release (versão, CHANGELOG, tag e release no GitHub) e rebuild do portfolio. Também é reconstruída toda segunda para pegar patches de segurança.
- **Dependências** — Renovate (job `platform/renovate` no Jenkins, `renovate.json` → preset do devops-platform): atualizações diárias, manutenção semanal do lockfile, issue "Dependency Dashboard" e auto-merge de patch/minor depois que o Jenkins aprova.

## Estrutura do projeto

```text
src/
  main.py                  # ponto de entrada da CLI
  pseudonymizer_service.py # fachada pública
  text_processor.py        # orquestra os detectores e a substituição
  detectors/
    entity_detector.py     # NER do spaCy (PERSON, GPE)
    phone_detector.py       # telefones via regex
    email_detector.py       # e-mails via regex
tests/                      # testes unitários (pytest, ~90%+ de cobertura)
```

## Casos de uso

- **Privacidade de dados**: mascarar PII antes de compartilhar, logar ou analisar texto.
- **GDPR & LGPD**: ajuda a atender regulações de proteção de dados.
- **Anonimização de texto**: anonimizar respostas de pesquisa, feedback de clientes ou documentos jurídicos.

## Referências

- [Medium – Demystifying Individual Privacy](https://medium.com/@nick.ruberg/demystifying-individual-privacy-anonymization-and-pseudonymization-in-the-age-of-data-protection-0bf7055fc0fd)
