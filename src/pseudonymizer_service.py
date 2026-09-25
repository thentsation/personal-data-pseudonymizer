from logger import setup_logging
from text_processor import TextProcessor


class PseudonymizerService:
    def __init__(self) -> None:
        self.processor = TextProcessor(logger=setup_logging())

    def pseudonymize_text(self, text: str) -> str:
        return self.processor.pseudonymize(text)
