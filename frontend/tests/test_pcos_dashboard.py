import streamlit as st
from pcos_dashboard import pcos_dashboard_page

def test_pcos_dashboard_page(monkeypatch):
    """
    Unit test for the `pcos_dashboard_page` function.
    This test ensures the dashboard page runs without raising errors
    by mocking all Streamlit UI-related components.
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
    pcos_dashboard_page()