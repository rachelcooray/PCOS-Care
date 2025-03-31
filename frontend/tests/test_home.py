import streamlit as st
from home import home_page

def test_home_page(monkeypatch):
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