import re

PHONE_PATTERN = re.compile(r"\+\d{1,2}\s?\(\d{1,3}\)\s?\d{3,4}-\d{4}")


class PhoneDetector:
    def detect_phone_numbers(self, text: str) -> list[str]:
        return PHONE_PATTERN.findall(text)
