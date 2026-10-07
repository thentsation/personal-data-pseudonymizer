# Personal Data Pseudonymizer

[![Python CI](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_docker.yaml)

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

O CI roda ruff, pytest (com piso de cobertura), mypy e pip-audit em todo push/PR, além de uma execução diária agendada. Imagens Docker são construídas, escaneadas com Trivy e publicadas no GHCR na `main`. O Dependabot mantém pip, imagem base do Docker e GitHub Actions atualizados, com bumps patch/minor mesclados automaticamente. Releases são versionados automaticamente com [python-semantic-release](https://python-semantic-release.readthedocs.io/) a partir de Conventional Commits.

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
