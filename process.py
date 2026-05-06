from common import validate_marker
from constants import INPUT_FILENAME, MARKER, OUTPUT_FILENAME


def main():
    """
    Entry point of the AStrip text normalization pipeline.

    This script processes a text file intended for Anki import by
    applying consistent normalization, deduplication, and sorting.

    Workflow:
        1. Validate both input and output files using a security marker
        to ensure they belong to this application.
        2. Open input and output files.
        3. Preserve the first line of the input file (session marker).
        4. Process remaining lines:
            - Normalize whitespace (collapse all whitespace into single spaces)
            - Convert text to lowercase
        5. Skip empty lines after normalization.
        6. Remove duplicate entries.
        7. Sort entries alphabetically.
        8. Write processed lines to the output file.

    Notes:
        - Input file is never modified.
        - Output file is overwritten on each run.
        - Whitespace normalization removes redundant spacing while preserving word boundaries.
        - Lowercasing ensures case-insensitive consistency.
        - Deduplication ensures each entry appears only once.
        - Sorting guarantees deterministic and predictable output order.
    """
    validate_marker(INPUT_FILENAME, MARKER)
    validate_marker(OUTPUT_FILENAME, MARKER)

    with (
        open(INPUT_FILENAME, "r", encoding="utf-8") as file_in,
        open(OUTPUT_FILENAME, "w", encoding="utf-8") as file_out,
    ):
        file_out.write(file_in.readline())

        word_set: set[str] = set()

        for line in file_in:
            correct_line: str = " ".join(line.split()).lower()

            if not correct_line:
                continue

            word_set.add(correct_line)
            
        words = list(word_set)
        words.sort()

        for word in words:
            file_out.write(word + "\n")


if __name__ == "__main__":
    main()
