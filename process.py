from common import validate_marker
from constants import INPUT_FILENAME, MARKER, OUTPUT_FILENAME


def main():
    """
    Entry point of the AStrip text normalization pipeline.

    The script processes a text file intended for Anki import by
    performing safe and consistent normalization of each line.

    Workflow:
        1. Validate both input and output files using a security marker
           to ensure they belong to this application.
        2. Open input and output files.
        3. Preserve the first line of the input file (session marker).
        4. Process remaining lines:
            - Split line by any whitespace (spaces, tabs, newlines)
            - Rejoin using a single space
            - Convert text to lowercase (normalization step)
        5. Skip empty lines after normalization.
        6. Write processed lines to the output file.

    Notes:
        - Input file is never modified.
        - Output file is overwritten on each run.
        - Whitespace normalization is strict and removes all redundant
          formatting while preserving word boundaries.
        - Lowercasing ensures case-insensitive consistency for Anki entries.
    """
    validate_marker(INPUT_FILENAME, MARKER)
    validate_marker(OUTPUT_FILENAME, MARKER)

    with (
        open(INPUT_FILENAME, "r", encoding="utf-8") as file_in,
        open(OUTPUT_FILENAME, "w", encoding="utf-8") as file_out,
    ):
        file_out.write(file_in.readline())

        for line in file_in:
            correct_line: str = " ".join(line.split()).lower()

            if correct_line == "":
                continue

            file_out.write(correct_line + "\n")


if __name__ == "__main__":
    main()
