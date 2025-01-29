import streamlit as st
import os

logo_path = "images/logo.png"

# Function to validate numeric inputs
def is_valid_number(value, min_value=None, max_value=None):
    try:
        value = float(value)
        if min_value is not None and value < min_value:
            return False
        if max_value is not None and value > max_value:
            return False
        return True
    except ValueError:
        return False

# Individual validation functions
def validate_age(age):
    if is_valid_number(age, 18, 75):
        return True
    return False

def validate_weight(weight):
    if is_valid_number(weight, 30, 200):
        return True
    return False

def validate_height(height):
    if is_valid_number(height, 100, 250):
        return True
    return False

def validate_bmi(bmi):
    if is_valid_number(bmi, 10, 50):
        return True
    return False

def validate_bp_systolic(bp_systolic):
    if is_valid_number(bp_systolic, 80, 200):
        return True
    return False

def validate_bp_diastolic(bp_diastolic):
    if is_valid_number(bp_diastolic, 50, 120):
        return True
    return False

def validate_pulse_rate(pulse_rate):
    return is_valid_number(pulse_rate, 40, 200)

def validate_respiratory_rate(rr_rate):
    return is_valid_number(rr_rate, 12, 30)

def validate_hemoglobin(hb):
    return is_valid_number(hb, 8, 18)

def validate_cycle_length(cycle_length):
    return is_valid_number(cycle_length, 21, 35)

def validate_marriage_years(marriage_years):
    return is_valid_number(marriage_years, 0, 60)

def validate_number_of_abortions(no_of_abortions):
    return is_valid_number(no_of_abortions, 0, 10)

def validate_hip(hip):
    return is_valid_number(hip, 20, 70)

def validate_waist(waist):
    return is_valid_number(waist, 20, 60)

def validate_waist_hip_ratio(waist_hip_ratio):
    return is_valid_number(waist_hip_ratio, 0.4, 1.0)
    
def simple_risk_assessment_page():
    col1, col2 = st.columns([1, 4])  

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Risk Assessment Tool")

    st.subheader("Simple Risk Assessment")
    st.markdown("""
    Provide basic health data and symptoms for a quick PCOS risk analysis. Enter the details as per the guidelines provided for each field.
    """)
    
    # Section breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Collect user input for simple risk assessment
    st.write("### General Information")
    age = st.text_input(
        "Age (years):", 
        placeholder="Enter your age (e.g., 25, whole number between 18-75)", 
        help="Enter your age as a whole number between 18 and 75."
    )
    weight = st.text_input(
        "Weight (Kg):", 
        placeholder="Enter your weight in kg (e.g., 60.5)", 
        help="Enter your weight in kilograms. Decimals are allowed."
    )
    height = st.text_input(
        "Height (Cm):", 
        placeholder="Enter your height in cm (e.g., 160.0)", 
        help="Enter your height in centimeters. Decimals are allowed."
    )
    bmi = st.text_input(
        "BMI:", 
        placeholder="Enter your BMI (e.g., 22.0)", 
        help="Enter your Body Mass Index (BMI). Decimals are allowed."
    )
    blood_group = st.selectbox(
        "Blood Group:", 
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], 
        placeholder="Enter your Blood Group",
        help="Select your blood group."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Symptoms")
    weight_gain = st.radio(
        "Weight Gain (Yes/No):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have experienced unusual or excessive weight gain recently."
    )
    hair_growth = st.radio(
        "Excessive Hair Growth (Yes/No):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have observed abnormal or excessive hair growth."
    )
    skin_darkening = st.radio(
        "Skin Darkening (Yes/No):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have noticed dark patches on your skin."
    )
    pimples = st.radio(
        "Pimples (Yes/No):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have frequent or severe acne outbreaks."
    )
    reg_exercise = st.radio(
        "Regular Exercise (Yes/No):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you exercise regularly (at least 3 times a week)."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Blood Pressure")
    bp_systolic = st.text_input(
        "BP Systolic (mmHg):", 
        placeholder="Enter systolic BP (e.g., 120)", 
        help="Enter your systolic blood pressure as a whole number between 80 and 200."
    )
    bp_diastolic = st.text_input(
        "BP Diastolic (mmHg):", 
        placeholder="Enter diastolic BP (e.g., 80)", 
        help="Enter your diastolic blood pressure as a whole number between 50 and 120."
    )
    
    # Validate inputs
    if st.button("Submit"):
        age_valid = validate_age(age)
        weight_valid = validate_weight(weight)
        height_valid = validate_height(height)
        bmi_valid = validate_bmi(bmi)
        bp_systolic_valid = validate_bp_systolic(bp_systolic)
        bp_diastolic_valid = validate_bp_diastolic(bp_diastolic)

        if not age_valid:
            st.error("Age must be a number between 18 and 75.")
        if not weight_valid:
            st.error("Weight must be a number between 30 and 200 Kg.")
        if not height_valid:
            st.error("Height must be a number between 100 and 250 cm.")
        if not bmi_valid:
            st.error("BMI must be a number between 10 and 50.")
        if not bp_systolic_valid:
            st.error("Systolic BP must be a number between 80 and 200 mmHg.")
        if not bp_diastolic_valid:
            st.error("Diastolic BP must be a number between 50 and 120 mmHg.")
        if not all([weight_gain, hair_growth, skin_darkening, pimples, reg_exercise]):
            st.error("Please answer all symptom-related questions.")

        # If all inputs are valid
        if all([
            age_valid, weight_valid, height_valid, bmi_valid,
            bp_systolic_valid, bp_diastolic_valid,
            weight_gain, hair_growth, skin_darkening, pimples, reg_exercise
        ]):
            st.session_state.risk_assessment_data = {
                "Age": age,
                "Weight": weight,
                "Height": height,
                "BMI": bmi,
                "Weight Gain": weight_gain,
                "Excessive Hair Growth": hair_growth,
                "Skin Darkening": skin_darkening,
                "Pimples": pimples,
                "Regular Exercise": reg_exercise,
                "BP Systolic": bp_systolic,
                "BP Diastolic": bp_diastolic
            }

            st.markdown("#### Collected Data Summary:")
            st.json(st.session_state.risk_assessment_data)

            with st.spinner("Processing your data..."):
                st.progress(50)
                st.success("Simple risk assessment complete!")