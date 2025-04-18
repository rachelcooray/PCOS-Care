import streamlit as st
from home import home_page

def test_home_page(monkeypatch):
    """
    Unit test for the `home_page` function.
    This test ensures that the function executes without error by mocking
    Streamlit functions that require a UI context.
    """
    
    # Mock Streamlit functions
    def mock_markdown(*args, **kwargs):
        pass
    
    def mock_subheader(*args, **kwargs):
        pass
    
    def mock_image(*args, **kwargs):
        pass
    
    def mock_columns(*args, **kwargs):
        return [mock_image, mock_image, mock_image]
    
    monkeypatch.setattr(st, "markdown", mock_markdown)
    monkeypatch.setattr(st, "subheader", mock_subheader)
    monkeypatch.setattr(st, "image", mock_image)
    monkeypatch.setattr(st, "columns", mock_columns)
    
    # Call the function
    home_page()