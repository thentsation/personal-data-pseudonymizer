[🇧🇷 Português](ARTIGO.md) | 🇺🇸 English

# Turning a SOLID-exercise script into an actual CLI

This project started as an architecture exercise: take a small problem — masking PII in text — and structure it in layers following SOLID. It did that job well. What it lacked was everything that separates "organized code" from "something I'd publish and trust": no tests, no typing, no way to run it without editing `main.py`, and no CI watching any of it.

## What I had

A `pseudonymizer/` package with clearly separated responsibilities — `NamedEntityDetector` (spaCy, PERSON/GPE), `PhoneDetector` and `EmailDetector` (regex), `TextProcessor` orchestrating the three, and `PseudonymizerService` as a facade — plus a root-level `main.py` that only printed a fixed sample text. No package `__init__`, no type hints, a single integration test (`test_pseudonymizer.py`) checking that three substrings disappeared from the output, and a misspelled `config/requeriments.txt` containing just `spacy`, unpinned.

It worked. But "works on my machine, for my sample text" is not a CLI — it's a demo.

## Giving an interface to something that only had a fixed example

The first decision was to stop pretending "running the project" meant "editing the source to change the text". `src/main.py` got a real argument parser with three ways to provide input — text as a positional argument, text via stdin (to compose with pipes), or `--sample` to reproduce the original example without memorizing the sentence:

```python
def resolve_input_text(args: argparse.Namespace) -> str:
    if args.sample:
        return SAMPLE_TEXT
    if args.text is not None:
        return args.text
    return sys.stdin.read()
```

It's a small CLI, but it's a CLI now — `echo "John Doe lives in Paris" | python src/main.py` works, and the Dockerfile uses exactly this contract (`ENTRYPOINT ["python", "src/main.py"]`, `CMD ["--sample"]` as the default).

## A safety net before anything new

I followed the same rule I apply to any productization: no new feature without a test underneath it. The single existing test exercised the whole system end to end; I split coverage by responsibility — `test_email_detector.py` and `test_phone_detector.py` test the regexes in isolation (including the "found nothing" case), `test_entity_detector.py` checks entity extraction and that the spaCy model is cached across instances (loading `en_core_web_sm` from disk isn't free), `test_text_processor.py` and `test_pseudonymizer_service.py` cover orchestration, and `test_main.py` tests the CLI (input resolution, stdin, `--sample`) without spawning a subprocess.

The result: 94% line coverage, without mocking spaCy — the model is small (`en_core_web_sm`) and deterministic enough that it's worth testing against the real model instead of a double.

Type hints everywhere (`disallow_untyped_defs = true` in mypy) forced naming types that were previously implicit — for instance, `NamedEntity = tuple[int, int, str]` instead of anonymous tuples scattered through the code.

## Model caching: a detail that almost slipped by

`NamedEntityDetector.__init__` called `spacy.load("en_core_web_sm")` on every instantiation. In a CLI that runs once and exits this doesn't matter, but in tests — which create multiple instances — every `spacy.load` costs tens of milliseconds. A simple module-level cache fixes both cases:

```python
_MODEL_CACHE: dict[str, Language] = {}

def _load_model(model_name: str) -> Language:
    if model_name not in _MODEL_CACHE:
        _MODEL_CACHE[model_name] = spacy.load(model_name)
    return _MODEL_CACHE[model_name]
```

## Packaging: downloading the model is a build-time concern, not a runtime one

The Dockerfile is multi-stage (`python:3.12-slim`), runs as a non-root user, and — a lesson borrowed from the other projects in the same family (the sentiment API pre-downloads the VADER lexicon at build time for the exact same reason) — downloads the spaCy model **during the image build**, not on the first request:

```dockerfile
RUN python -m spacy download en_core_web_sm
```

Without this, the first `docker run` anywhere would depend on network access being available at runtime.

## CI, dependabot and release, so I don't have to remember

The pipeline (`pipeline_python.yaml`) runs ruff (lint + format check), pytest with a 90% coverage floor, mypy and pip-audit — on every PR, every push, and once a day on a schedule. The Docker pipeline builds, scans with Trivy, and publishes to GHCR once the Python CI passes on `main`. Dependabot covers pip, the Docker base image, and the GitHub Actions themselves, with patch/minor bumps auto-merged and majors labeled for manual review in a dashboard issue that updates (and closes) itself. Releases follow semver automatically via Conventional Commits, starting here at `v1.0.0`.

## What I left out, for now

I did not wire an automatic `deploy.yaml` on push — unlike the sentiment API or the chatbot, this CLI isn't a long-running service that needs to stay up; the deploy workflow exists as a manual `workflow_dispatch` that only runs the published image as a smoke test against the sample text, without touching production infrastructure unless I explicitly ask for it.
