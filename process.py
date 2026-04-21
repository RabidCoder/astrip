from common import validate_marker
from constants import INPUT_FILENAME, MARKER, OUTPUT_FILENAME


def main():
    validate_marker(INPUT_FILENAME, MARKER)
    validate_marker(OUTPUT_FILENAME, MARKER)
    print("everything is allright")


if __name__ == "__main__":
    main()
