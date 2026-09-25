import io
from contextlib import redirect_stdout

import main


def test_resolve_input_text_prefers_sample_flag() -> None:
    args = main.build_parser().parse_args(["--sample"])
    assert main.resolve_input_text(args) == main.SAMPLE_TEXT


def test_resolve_input_text_uses_positional_argument() -> None:
    args = main.build_parser().parse_args(["hello world"])
    assert main.resolve_input_text(args) == "hello world"


def test_resolve_input_text_reads_stdin_when_no_args(monkeypatch) -> None:
    monkeypatch.setattr("sys.stdin", io.StringIO("from stdin"))
    args = main.build_parser().parse_args([])
    assert main.resolve_input_text(args) == "from stdin"


def test_main_prints_original_and_pseudonymized_text() -> None:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        main.build_parser().parse_args(["--sample"])
        import sys

        sys.argv = ["pseudonymizer", "--sample"]
        main.main()

    output = buffer.getvalue()
    assert "Original text:" in output
    assert "Pseudonymized text:" in output
    assert "John Doe" not in output.split("Pseudonymized text:")[1]
