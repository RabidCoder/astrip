import os

# --- Configuration ---
FILENAME = "INPUT.txt"
MARKER = "# --- ASTRIP SESSION ---\n"


class ForeignFileError(Exception):
    """
    Raised when the target file exists but does not contain
    the required application signature.
    """
    pass


def create_new_file(marker, filename):
    """
    Creates new file and initializs it with the session marker.
    
    Args:
        marker (str): The unique header string to identify the file.
        filename (str): The name of the file to be created.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(marker)
    
    print(f"[SUCCESS] Workspace {FILENAME} cleared and ready for new data.")


def main():
    """
    Orchestrates the workspace preparation.

    1. Checks for existence of the input file.
    2. Validates the security marker to prevent overwriting user data.
    3. Clears the file if it belongs to AStrip, preparing it for a new batch.
    """
    if not os.path.exists(FILENAME):
        # Initial setup
        create_new_file(MARKER, FILENAME)
    else:
        # Safety check
        with open(FILENAME, "r", encoding="utf-8") as f:
            first_line = f.readline()
            if first_line != MARKER:
                # Prevent data corruption of non-AStrip files
                raise ForeignFileError(
                    "Danger! This file was not created by AStrip. Aborting to pretect data."
                )
            else:
                # Refresh the buffer for the next input session
                create_new_file(MARKER, FILENAME)


if __name__ == "__main__":
    main()
