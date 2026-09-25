import re

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")


class EmailDetector:
    def detect_emails(self, text: str) -> list[str]:
        return EMAIL_PATTERN.findall(text)
