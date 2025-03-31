import streamlit as st
from enhanced_risk_assessment import enhanced_risk_assessment_page

def test_enhanced_risk_assessment_page(monkeypatch):
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
    enhanced_risk_assessment_page()