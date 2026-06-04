import unittest
from asci_art.converter import image_to_ascii
import os

class TestImageToAscii(unittest.TestCase):

    def setUp(self):
        self.test_image = "img/user.webp"  # A small grayscale image for testing
        self.default_signature = "GRX"

    def test_basic_conversion(self):
        ascii_art = image_to_ascii(
            image_path=self.test_image,
            width=64,
            contrast=1.5,
            signature=self.default_signature,
            palette="@%#*+=-:. "
        )
        self.assertIsInstance(ascii_art, str)
        self.assertIn(self.default_signature, ascii_art)

    def test_custom_palette(self):
        palette = "█▓▒░ "
        signature = "test"
        ascii_art = image_to_ascii(
            image_path=self.test_image,
            width=32,
            contrast=1.0,
            signature=signature,
            palette=palette
        )
        for char in ascii_art:
            if char not in "\n":
                self.assertIn(char, palette + signature)


    def test_empty_palette_fallback(self):
        ascii_art = image_to_ascii(
            image_path=self.test_image,
            width=32,
            contrast=1.0,
            signature="Fallback",
            palette=""
        )
        self.assertIn("Fallback", ascii_art)

    def test_invalid_image_path(self):
        with self.assertRaises(FileNotFoundError):
            image_to_ascii(
                image_path="img/does_not_exist.jpg",
                width=32,
                contrast=1.0,
                signature="Error",
                palette="@#* "
            )

if __name__ == "__main__":
    unittest.main()

#python3 -m unittest discover -s tests