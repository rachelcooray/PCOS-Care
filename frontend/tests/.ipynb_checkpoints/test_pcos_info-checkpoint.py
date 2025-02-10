import unittest
from unittest.mock import patch
import pcos_info
import os

class TestPcosInfo(unittest.TestCase):
    
    @patch("os.path.exists", return_value=True)
    def test_logo_exists(self, mock_exists):
        self.assertTrue(os.path.exists("images/logo.png"))
    
    @patch("os.path.exists", return_value=False)
    def test_logo_not_exists(self, mock_exists):
        self.assertFalse(os.path.exists("images/logo.png"))

if __name__ == "__main__":
    unittest.main()
