import streamlit as st
from results import results_page

def test_results_page(monkeypatch):
    """
    Test the `results_page` function by mocking essential Streamlit components.
    To verify that the results page executes successfully without rendering actual UI elements.
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
    results_page()