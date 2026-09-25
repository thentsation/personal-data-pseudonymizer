import argparse
import sys

from pseudonymizer_service import PseudonymizerService

SAMPLE_TEXT = (
    "The applicant John Doe, living at Maple Street, has the phone number "
    "+1 (415) 555-1234, and his email is john.doe@example.com. He also visited New York."
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pseudonymizer",
        description="Pseudonymize names, locations, phone numbers and emails in free text.",
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text to pseudonymize. Reads from stdin if omitted and --sample is not set.",
    )
    parser.add_argument(
        "--sample",
        action="store_true",
        help="Run against the built-in sample text instead of stdin/argument.",
    )
    return parser


def resolve_input_text(args: argparse.Namespace) -> str:
    if args.sample:
        return SAMPLE_TEXT
    if args.text is not None:
        return args.text
    return sys.stdin.read()


def main() -> None:
    args = build_parser().parse_args()
    text = resolve_input_text(args)

    service = PseudonymizerService()
    pseudonymized_text = service.pseudonymize_text(text)

    print("Original text:")
    print(text)
    print("\nPseudonymized text:")
    print(pseudonymized_text)


if __name__ == "__main__":
    main()
