from detectors.entity_detector import NamedEntityDetector


def test_extracts_person_and_location() -> None:
    detector = NamedEntityDetector()
    entities = detector.extract_named_entities("John Doe visited New York.")
    labels = {label for _, _, label in entities}
    assert "PERSON" in labels
    assert "GPE" in labels


def test_reuses_cached_model_instance() -> None:
    first = NamedEntityDetector()
    second = NamedEntityDetector()
    assert first.nlp is second.nlp
