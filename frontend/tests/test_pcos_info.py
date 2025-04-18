import pytest
from unittest.mock import MagicMock
import streamlit as st
from pcos_info import pcos_info_page

def test_pcos_info_page(monkeypatch):
    """
    Unit test for the `pcos_info_page` function.
    This test checks whether the function runs without error by mocking
    Streamlit functions that rely on the app's frontend rendering.
    """
    
    # Mock Streamlit functions
    def mock_markdown(*args, **kwargs):
        pass
    
    def mock_subheader(*args, **kwargs):
        pass
    
    def mock_image(*args, **kwargs):
        pass
    
    # Mock columns to return mock objects
    def mock_columns(*args, **kwargs):
        return [MagicMock(), MagicMock(), MagicMock()]  # Mocking the columns
    
    monkeypatch.setattr(st, "markdown", mock_markdown)
    monkeypatch.setattr(st, "subheader", mock_subheader)
    monkeypatch.setattr(st, "image", mock_image)
    monkeypatch.setattr(st, "columns", mock_columns)
    
    # Call the function
    pcos_info_page()
