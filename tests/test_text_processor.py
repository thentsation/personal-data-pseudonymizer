from text_processor import TextProcessor


def test_pseudonymizes_person_email_and_phone() -> None:
    processor = TextProcessor()
    text = (
        "The applicant John Doe, living at Maple Street, has the phone number "
        "+1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York."
    )
    result = processor.pseudonymize(text)

    assert "John Doe" not in result
    assert "New York" not in result
    assert "+1 (415) 555-1234" not in result
    assert "john.doe@example.com" not in result


def test_leaves_text_without_pii_unchanged() -> None:
    processor = TextProcessor()
    text = "This sentence has no personal data at all."
    assert processor.pseudonymize(text) == text
