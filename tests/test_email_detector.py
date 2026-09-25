from detectors.email_detector import EmailDetector


def test_detects_single_email() -> None:
    detector = EmailDetector()
    assert detector.detect_emails("Contact: john.doe@example.com please.") == [
        "john.doe@example.com"
    ]


def test_detects_multiple_emails() -> None:
    detector = EmailDetector()
    emails = detector.detect_emails("a@example.com and b@test.org")
    assert emails == ["a@example.com", "b@test.org"]


def test_returns_empty_list_when_no_email() -> None:
    detector = EmailDetector()
    assert detector.detect_emails("no emails here") == []
