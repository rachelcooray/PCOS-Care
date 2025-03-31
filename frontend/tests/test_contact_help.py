import streamlit as st
from contact_help import contact_help_page

def test_contact_help_page(monkeypatch):
    # Mock Streamlit functions
    def mock_markdown(*args, **kwargs):
        pass
    
    def mock_subheader(*args, **kwargs):
        pass
    
    def mock_expander(*args, **kwargs):
        class MockExpander:
            def __enter__(self):
                return self
            def __exit__(self, exc_type, exc_val, exc_tb):
                pass
            def markdown(self, *args, **kwargs):
                pass
        return MockExpander()
    
    monkeypatch.setattr(st, "markdown", mock_markdown)
    monkeypatch.setattr(st, "subheader", mock_subheader)
    monkeypatch.setattr(st, "expander", mock_expander)
    
    # Call the function
    contact_help_page()