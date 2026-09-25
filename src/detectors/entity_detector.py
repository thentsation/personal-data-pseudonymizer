import spacy
from spacy.language import Language

NamedEntity = tuple[int, int, str]

_MODEL_CACHE: dict[str, Language] = {}


def _load_model(model_name: str) -> Language:
    if model_name not in _MODEL_CACHE:
        _MODEL_CACHE[model_name] = spacy.load(model_name)
    return _MODEL_CACHE[model_name]


class NamedEntityDetector:
    def __init__(self, model_name: str = "en_core_web_sm") -> None:
        self.nlp = _load_model(model_name)

    def extract_named_entities(self, text: str) -> list[NamedEntity]:
        doc = self.nlp(text)
        return [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
