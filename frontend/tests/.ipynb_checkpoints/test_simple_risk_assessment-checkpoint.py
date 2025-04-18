import streamlit as st
from simple_risk_assessment import simple_risk_assessment_page

def test_simple_risk_assessment_page(monkeypatch):
    """
    Unit test for the `simple_risk_assessment_page` function.
    This test ensures that the page loads and executes without errors by mocking
    Streamlit UI components like input fields, radio buttons, and dropdowns.
    """

    # Mock session state
    st.session_state.form_data = {
        "age": "25",
        "weight": "60",
        "height": "160",
        "blood_group": "A+",
        "pulse_rate": "72",
        "rr_rate": "18",
        "cycle": "Regular"
    }

    # Initialize symptom session state
    st.session_state.weight_gain = "Yes"
    st.session_state.hair_growth = "Yes"
    st.session_state.skin_darkening = "Yes"
    st.session_state.hair_loss = "Yes"
    st.session_state.pimples = "Yes"
    st.session_state.fast_food = "Yes"
    st.session_state.reg_exercise = "Yes"

    # Mock Streamlit functions
    monkeypatch.setattr(st, "markdown", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(st, "text_input", lambda *args, **kwargs: "")
    monkeypatch.setattr(st, "radio", lambda *args, **kwargs: "Yes")
    monkeypatch.setattr(st, "selectbox", lambda label, options, index=0, help=None: options[index])
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: None)

    # Call the function
    simple_risk_assessment_page()
