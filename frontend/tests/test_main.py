import streamlit as st
import pytest
from unittest.mock import patch, MagicMock

from home import home_page
from pcos_info import pcos_info_page
from simple_risk_assessment import simple_risk_assessment_page
from enhanced_risk_assessment import enhanced_risk_assessment_page
from results import results_page
from contact_help import contact_help_page
from pcos_dashboard import pcos_dashboard_page

# Mock Streamlit functions to prevent actual UI rendering in tests
@pytest.fixture
def mock_streamlit(monkeypatch):
    """
    This fixture mocks key Streamlit functions to prevent actual UI rendering during tests.
    The purpose is to isolate the logic of the page navigation and session state management
    without rendering the actual UI components.
    """
    def mock_func(*args, **kwargs):
        return None
    
    # Create a mock column object that supports `with` statements
    mock_column = MagicMock()
    mock_column.__enter__.return_value = mock_column
    mock_column.__exit__.return_value = None
    
    monkeypatch.setattr(st, "markdown", mock_func)
    monkeypatch.setattr(st, "subheader", mock_func)
    monkeypatch.setattr(st, "image", mock_func)
    monkeypatch.setattr(st, "error", mock_func)
    monkeypatch.setattr(st, "stop", mock_func)
    
    # Mock `st.columns` to return a list of three mock columns
    monkeypatch.setattr(st, "columns", lambda *args, **kwargs: [mock_column, mock_column, mock_column])


def test_page_navigation(mock_streamlit):
    """
    Test that different pages in the app can be selected and rendered without errors.
    This ensures that when a user selects a page, the corresponding page function runs
    correctly and doesn't throw any exceptions.
    """
    pages = {
        "Home": home_page,
        "PCOS Information": pcos_info_page,
        "Insights From Data": pcos_dashboard_page,
        "Simple Risk Assessment": simple_risk_assessment_page,
        "Enhanced Risk Assessment": enhanced_risk_assessment_page,
        "Your Results": results_page,
        "Help & Contact": contact_help_page,
    }

    for page_name, page_function in pages.items():
        with patch("streamlit_navigation_bar.st_navbar", return_value=page_name):
            # Properly mock `st.session_state` to behave like an object
            mock_session_state = MagicMock()
            mock_session_state.page = page_name
            mock_session_state.form_data = {}  # Add form_data to avoid AttributeError

            with patch("streamlit.session_state", mock_session_state):
                page_function()  # Ensure the function runs without errors
