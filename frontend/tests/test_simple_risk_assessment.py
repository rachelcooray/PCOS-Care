import streamlit as st
from simple_risk_assessment import simple_risk_assessment_page

def test_simple_risk_assessment_page(monkeypatch):
    """
    Unit test for the `simple_risk_assessment_page` function.
    This test ensures that the page loads and executes without errors by mocking
    Streamlit UI components like input fields, radio buttons, and dropdowns.
    """
    
    # Mock Streamlit functions
    def mock_markdown(*args, **kwargs):
        pass
    
    def mock_subheader(*args, **kwargs):
        pass
    
    def mock_text_input(*args, **kwargs):
        return ""
    
    def mock_radio(*args, **kwargs):
        return "Yes"
    
    def mock_selectbox(*args, **kwargs):
        return "A+"
    
    monkeypatch.setattr(st, "markdown", mock_markdown)
    monkeypatch.setattr(st, "subheader", mock_subheader)
    monkeypatch.setattr(st, "text_input", mock_text_input)
    monkeypatch.setattr(st, "radio", mock_radio)
    monkeypatch.setattr(st, "selectbox", mock_selectbox)
    
    # Call the function
    simple_risk_assessment_page()