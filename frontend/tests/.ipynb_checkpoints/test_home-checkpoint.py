import unittest
from unittest.mock import patch, MagicMock
import home
import os
from PIL import Image

class TestHome(unittest.TestCase):
    
    @patch("os.path.exists", return_value=True)
    @patch("PIL.Image.open")
    def test_load_and_resize_image_exists(self, mock_open, mock_exists):
        mock_image = MagicMock()
        mock_open.return_value = mock_image
        
        result = home.load_and_resize_image("images/logo.png")
        
        self.assertIsNotNone(result)
        mock_open.assert_called_once()
        mock_image.resize.assert_called_once_with((150, 150))

    @patch("os.path.exists", return_value=False)
    def test_load_and_resize_image_not_exists(self, mock_exists):
        result = home.load_and_resize_image("images/nonexistent.png")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()