from common import prepare_workspace
from constants import INPUT_FILENAME, OUTPUT_FILENAME, MARKER


def main():
    # Prepare input file:
    prepare_workspace(INPUT_FILENAME, MARKER)
    # Prepare output file:
    prepare_workspace(OUTPUT_FILENAME, MARKER)


if __name__ == "__main__":
    main()
