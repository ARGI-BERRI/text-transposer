import sys
from pathlib import Path


def transpose_to_vertical(input_file: Path) -> str:
    """Transpose horizontal text to vertical text.

    In other words, transpose from LTR text to TTB text with RTL order. <br />
    If the length of each line is different, the shorter lines will be padded with full-width spaces.

    Args:
        input_file (Path): The path to the input text file.

    Raises:
        FileNotFoundError: Raises if the specified file does not exist.
        RuntimeError: Raises if an error occurs while reading the file.

    Returns:
        str: The transposed text.
    """
    try:
        content = input_file.read_text(encoding="utf-8")

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {input_file}")

    except Exception as e:
        raise RuntimeError(f"Error occurred while reading the file: {e}") from e

    lines = content.splitlines()
    if not lines or all(not line.strip() for line in lines):
        return ""

    max_length = max((len(line) for line in lines), default=0)
    padded_lines = [line.ljust(max_length, "　") for line in lines]

    transposed = "\n".join("".join(row) for row in zip(*reversed(padded_lines)))
    return transposed


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = Path(sys.argv[1])

    else:
        input_path = Path("./resources/original.txt")

    print(transpose_to_vertical(input_path))
