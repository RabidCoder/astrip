import os


class ForeignFileError(Exception):
    """
    Raised when a file already exists but does not contain the expected marker,
    indicating it was not created by this program.
    """

    pass


def create_new_file(filename, marker):
    """
    Create or overwrite a file and initialize it with a marker.

    This function is used both for initial file creation and for
    resetting an existing, validated workspace file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(marker)

    print(f"[SUCCESS] Workspace {filename} cleared and ready for new data.")


def validate_marker(filename, marker):
    """
    Validate that the file belongs to this application by checking its marker.

    The expected marker must be located on the first line of the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        first_line: str = f.readline()

        if first_line != marker:
            raise ForeignFileError(
                "File is not recognized as a valid workspace file. Aborting to prevent data loss."
            )


def prepare_workspace(filename, marker):
    """
    Prepare a workspace file for use.

    Behavior:
        1. If the file does not exist → create it with the marker.
        2. If the file exists:
            - validate that it belongs to this program (via marker)
            - if valid → reset (overwrite) it
            - if invalid → raise an error to prevent data loss
    """
    if not os.path.exists(filename):
        create_new_file(filename, marker)
        return

    # Ensure file belongs to this application
    validate_marker(filename, marker)

    # If we got here → file is valid
    create_new_file(filename, marker)
