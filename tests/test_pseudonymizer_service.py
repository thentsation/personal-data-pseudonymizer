from pseudonymizer_service import PseudonymizerService


def test_pseudonymize_text_delegates_to_processor() -> None:
    service = PseudonymizerService()
    text = (
        "John Doe's email is john.doe@example.com and his phone is +1 (123) 456-7890."
    )
    result = service.pseudonymize_text(text)

    assert "John Doe" not in result
    assert "john.doe@example.com" not in result
    assert "+1 (123) 456-7890" not in result
