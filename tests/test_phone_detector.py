from detectors.phone_detector import PhoneDetector


def test_detects_phone_number() -> None:
    detector = PhoneDetector()
    numbers = detector.detect_phone_numbers("Call +1 (415) 555-1234 now.")
    assert numbers == ["+1 (415) 555-1234"]


def test_returns_empty_list_when_no_phone() -> None:
    detector = PhoneDetector()
    assert detector.detect_phone_numbers("no phone here") == []
