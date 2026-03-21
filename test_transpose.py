import unittest
from pathlib import Path

from transpose import transpose_to_vertical


class TestTransposeFile(unittest.TestCase):
    def test_transpose_file(self):
        correct_transposed_text = Path("./resources/transposed.txt").read_text(
            encoding="utf-8"
        )
        transposed_text = transpose_to_vertical(Path("./resources/original.txt"))

        self.assertEqual(correct_transposed_text, transposed_text)


if __name__ == "__main__":
    unittest.main()
