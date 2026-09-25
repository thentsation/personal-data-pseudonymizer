import logging


def setup_logging() -> logging.Logger:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    return logging.getLogger("Pseudonymizer")
