# Personal Data Pseudonymizer

[![Python CI](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/personal-data-pseudonymizer/actions/workflows/pipeline_docker.yaml)

> Leia em [português](README.pt-br.md).

A small Python CLI that uses spaCy to find named entities in English text and replaces them with pseudonyms (asterisks), together with phone numbers and email addresses. The goal is to protect personally identifiable information (PII) before text is shared, logged, or analyzed.

An in-depth write-up of the design and productization of this project is available in [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Features

- Detects **people (PERSON)** and **locations (GPE)** with spaCy's named entity recognition.
- Detects phone numbers and email addresses with regular expressions.
- Replaces every match with asterisks of the same length, preserving the original text layout.
- Ships as a small CLI (`src/main.py`) and as a reusable library (`PseudonymizerService`).

### Sample output

```text
Original text:
The applicant John Doe, living at Maple Street, has the phone number +1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York.

Pseudonymized text:
The applicant **** ** ***, living at ***** Street, has the phone number ************, and his email is ********@*****.***. He also visited ***** York.
```

## Getting started

```bash
make install       # creates .venv, installs deps and the spaCy model
make run           # runs the CLI against the built-in sample text
echo "John Doe lives in Paris" | make run  # or: .venv/bin/python src/main.py
```

Run with Docker instead:

```bash
make docker-build
make docker-run
```

## Development

```bash
make test        # pytest
make coverage     # pytest with coverage report
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI runs ruff, pytest (coverage gate), mypy and pip-audit on every push/PR, plus a scheduled daily run. Docker images are built, scanned with Trivy, and published to GHCR on `main`. Dependabot keeps pip, Docker base image, and GitHub Actions versions up to date, with patch/minor bumps auto-merged. Releases are tagged automatically with [python-semantic-release](https://python-semantic-release.readthedocs.io/) based on Conventional Commits.

## Project layout

```text
src/
  main.py                  # CLI entry point
  pseudonymizer_service.py # public facade
  text_processor.py        # orchestrates detectors and replacement
  detectors/
    entity_detector.py     # spaCy NER (PERSON, GPE)
    phone_detector.py       # regex phone numbers
    email_detector.py       # regex emails
tests/                      # unit tests (pytest, ~90%+ coverage)
```

## Use cases

- **Data privacy**: mask PII in text before sharing, logging, or analyzing it.
- **GDPR & LGPD**: helps support compliance with data protection regulations.
- **Text anonymization**: anonymize survey responses, customer feedback, or legal documents.

## References

- [Medium – Demystifying Individual Privacy](https://medium.com/@nick.ruberg/demystifying-individual-privacy-anonymization-and-pseudonymization-in-the-age-of-data-protection-0bf7055fc0fd)
