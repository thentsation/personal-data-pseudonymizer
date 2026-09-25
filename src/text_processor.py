import logging

from detectors.email_detector import EmailDetector
from detectors.entity_detector import NamedEntityDetector
from detectors.phone_detector import PhoneDetector

PSEUDONYMIZED_ENTITY_LABELS = {"PERSON", "GPE"}


class TextProcessor:
    def __init__(self, logger: logging.Logger | None = None) -> None:
        self.logger = logger or logging.getLogger("Pseudonymizer")
        self.entity_detector = NamedEntityDetector()
        self.phone_detector = PhoneDetector()
        self.email_detector = EmailDetector()

    def pseudonymize(self, text: str) -> str:
        self.logger.info("Starting text pseudonymization.")

        entities = self.entity_detector.extract_named_entities(text)
        phone_numbers = self.phone_detector.detect_phone_numbers(text)
        email_addresses = self.email_detector.detect_emails(text)

        for start, end, label in reversed(entities):
            if label in PSEUDONYMIZED_ENTITY_LABELS:
                text = text[:start] + "*" * (end - start) + text[end:]
                self.logger.info("Pseudonymized entity (type: %s)", label)

        for phone in phone_numbers:
            text = text.replace(phone, "*" * len(phone))
            self.logger.info("Pseudonymized phone number")

        for email in email_addresses:
            text = text.replace(email, "*" * len(email))
            self.logger.info("Pseudonymized email address")

        self.logger.info("Pseudonymization complete.")
        return text
