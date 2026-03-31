import re


def count_file_lines(filename: str) -> int:
    """Read a file and count how many sentence-like lines it has.

    The text is split by '.', '?', and '!'. Empty pieces are ignored.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            raw_lines = re.split(r"[.?!]", content)
            lines = [s.strip() for s in raw_lines if s.strip()]
            print("total lines", len(lines))

    except FileNotFoundError:
        print("file was not found")


count_file_lines("../textfile.txt")
