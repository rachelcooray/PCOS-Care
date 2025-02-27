import streamlit as st
import os
import requests
import json

# Function to send data to Flask API and get prediction
def get_prediction(input_data):
    # url = "http://127.0.0.1:5000/predict-simple"  # Flask API endpoint - localhost
    url = "https://pcos-care.onrender.com/predict-simple" # render
    # url = "https://rachelcooray.pythonanywhere.com/predict-simple"
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=input_data, headers=headers)
        
        if response.status_code == 200:
            prediction = response.json().get('prediction')
            return prediction
        else:
            return f"Error: {response.json().get('error')}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

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
    if is_valid_number(age, 18, 55):
        return True
    return False

def validate_weight(weight):
    if is_valid_number(weight, 30, 200):
        return True
    return False

def validate_height(height):
    if is_valid_number(height, 90, 250):
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
    return is_valid_number(pulse_rate, 15, 120)

def validate_respiratory_rate(rr_rate):
    return is_valid_number(rr_rate, 12, 30)

def validate_cycle(cycle):
    return cycle in ["Regular", "Irregular"]

def validate_cycle_length(cycle_length):
    return is_valid_number(cycle_length, 0, 14)

def validate_marriage_years(marriage_years):
    return is_valid_number(marriage_years, 0, 37)

def validate_number_of_abortions(no_of_abortions):
    return is_valid_number(no_of_abortions, 0, 5)

def validate_hip(hip):
    return is_valid_number(hip, 20, 60)

def validate_waist(waist):
    return is_valid_number(waist, 25, 55)

def validate_waist_hip_ratio(waist_hip_ratio):
    return is_valid_number(waist_hip_ratio, 0.5, 1.0)

def convert_yes_no(value):
    return 1 if value == "Yes" else 0

def convert_cycle(value):
    return 2 if value == "Regular" else 4

def convert_blood_group(value):
    blood_group_mapping = {
        "A+": 11,
        "A-": 12,
        "B+": 13,
        "B-": 14,
        "O+": 15,
        "O-": 16,
        "AB+": 17,
        "AB-": 18
    }
    return blood_group_mapping.get(value, None)

def calculate_bmi(weight, height):
    weight = float(weight) 
    height = float(height)
    return (weight / ((height/100) ** 2))

def calculate_waist_hip_ratio(waist, hip):
    waist = float(waist)
    hip = float(hip)
    return (waist / hip)
    
def simple_risk_assessment_page():
    col1, col2 = st.columns([1, 4])  

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    st.subheader("Simple Risk Assessment")
    st.markdown("""
    Provide basic health data and symptoms for a quick PCOS risk analysis. Enter the details in the feilds below.
    
    Guidelines have been provided for each field.
    """)
    
    # Section breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Collect user input for simple risk assessment
    st.write("### General Information")
    age = st.text_input(
        "Age (years):", 
        placeholder="25", 
        help="Enter your age as a whole number between 18 and 50."
    )
    weight = st.text_input(
        "Weight (Kg):", 
        placeholder="60.5", 
        help="Enter your weight in kilograms. Decimals are allowed."
    )
    height = st.text_input(
        "Height (Cm):", 
        placeholder="160.5", 
        help="Enter your height in centimeters. Decimals are allowed."
    )
    # bmi = st.text_input(
    #     "BMI:", 
    #     placeholder="22.8", 
    #     help="Enter your Body Mass Index (BMI). Decimals are allowed."
    # )
    blood_group = st.selectbox(
        "Blood Group:", 
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], 
        placeholder="Enter your Blood Group",
        help="Select your blood group."
    )
    pulse_rate = st.text_input(
        "Pulse rate(bpm):", 
        placeholder="72.0", 
        help="Enter your pulse rate in beats per minute. Decimals are allowed."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Symptoms")
    weight_gain = st.radio(
        "Have you experienced unusual or excessive weight gain recently?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have experienced unusual or excessive weight gain recently."
    )
    hair_growth = st.radio(
        "Have you observed abnormal or excessive hair growth?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have observed abnormal or excessive hair growth."
    )
    skin_darkening = st.radio(
        "Have you experienced any skin darkening?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have noticed dark patches on your skin."
    )
    hair_loss = st.radio(
        "Have you observed abnormal or excessive hair loss?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have observed abnormal or excessive hair loss."
    )
    pimples = st.radio(
        "Do you have frequent or severe acne outbreaks?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have frequent or severe acne outbreaks."
    )
    fast_food = st.radio(
        "Do you eat alot of fast food", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you eat alot of fast food."
    )
    reg_exercise = st.radio(
        "Do you exercise regularly?", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you exercise regularly (at least 3 times a week)."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Additional Information")
    
    rr_rate = st.text_input(
        "RR (breaths/min):", 
        placeholder="18", 
        help="Enter your respiratory rate in breaths per minute."
    )
    
    cycle = st.selectbox(
        "Cycle (R/I):", ["Regular", "Irregular"], 
        help="Select the cycle type as regular or irregular."
    )
    
    cycle_length = st.text_input(
        "Cycle length (days):", 
        placeholder="7", 
        help="Enter the number of days your menstrual period typically lasts."
    )
    
    marriage_years = st.text_input(
        "Marriage Status (Yrs):", 
        placeholder="0", 
        help="Enter the number of years of marriage."
    )
    
    pregnancy_status = st.radio(
        "Have you ever been pregnant?", 
        ["Yes", "No"], 
        index=None, 
        help="Select if pregnant (Y) or not (N)."
    )

    no_of_abortions = st.text_input(
        "No. of Abortions:", 
        placeholder="0", 
        help="Enter the number of abortions (if any)."
    )
    
    hip = st.text_input(
        "Hip (inch):", 
        placeholder="36", 
        help="Enter the hip measurement in inches."
    )
    
    waist = st.text_input(
        "Waist (inch):", 
        placeholder="32", 
        help="Enter the waist measurement in inches."
    )
    
    # waist_hip_ratio = st.text_input(
    #     "Waist:Hip Ratio:", 
    #     placeholder="0.8", 
    #     help="Enter your waist-to-hip ratio."
    # )

    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Blood Pressure")
    bp_systolic = st.text_input(
        "BP Systolic (mmHg):", 
        placeholder="120", 
        help="Enter your systolic blood pressure as a whole number between 80 and 200."
    )
    bp_diastolic = st.text_input(
        "BP Diastolic (mmHg):", 
        placeholder="80", 
        help="Enter your diastolic blood pressure as a whole number between 50 and 120."
    )
    
    # Validate inputs
    if st.button("Submit"):
        bmi = calculate_bmi(weight, height)
        waist_hip_ratio = calculate_waist_hip_ratio(waist, hip)
    
        age_valid = validate_age(age)
        weight_valid = validate_weight(weight)
        height_valid = validate_height(height)
        bmi_valid = validate_bmi(bmi)
        bp_systolic_valid = validate_bp_systolic(bp_systolic)
        bp_diastolic_valid = validate_bp_diastolic(bp_diastolic)
        pulse_rate_valid = validate_pulse_rate(pulse_rate)
        rr_valid = validate_respiratory_rate(rr_rate)
        cycle_valid = validate_cycle(cycle)
        cycle_length_valid = validate_cycle_length(cycle_length)
        marriage_years_valid = validate_marriage_years(marriage_years)
        no_of_abortions_valid = validate_number_of_abortions(no_of_abortions)
        hip_valid = validate_hip(hip)
        waist_valid = validate_waist(waist)
        waist_hip_ratio_valid = validate_waist_hip_ratio(waist_hip_ratio)

        # Collect errors
        errors = []
        if not age_valid: errors.append("Age must be between 18 and 55.")
        if not weight_valid: errors.append("Weight must be between 30 and 200 Kg.")
        if not height_valid: errors.append("Height must be between 90 and 250 cm.")
        # if not bmi_valid: errors.append("BMI must be between 10 and 50.")
        if not bp_systolic_valid: errors.append("BP systolic must be between 80 and 200 mmHg.")
        if not bp_diastolic_valid: errors.append("BP diastolic must be between 50 and 120 mmHg.")
        if not pulse_rate_valid: errors.append("Pulse rate must be between 15 and 120 bpm.")
        if not rr_valid: errors.append("Respiratory rate must be between 12 and 30 breaths per minute.")
        if not cycle_valid: errors.append("Cycle must be either 'Regular' or 'Irregular'.")
        if not cycle_length_valid: errors.append("Cycle length must be between 0 and 14 days.")
        if not marriage_years_valid: errors.append("Years of marriage must be between 0 and 37.")
        if not no_of_abortions_valid: errors.append("Number of abortions must be between 0 and 5.")
        if not hip_valid: errors.append("Hip measurement must be between 20 and 60 inches.")
        if not waist_valid: errors.append("Waist measurement must be between 20 and 55 inches.")
        # if not waist_hip_ratio_valid: errors.append("Waist to hip ratio must be between 0.5 and 1.0.")

        # Show errors if any
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("All inputs are valid! Form submitted successfully.")
            
            data = {
                " Age (yrs)": age,
                "Weight (Kg)": weight,
                "Height(Cm) ": height,
                "BMI": bmi,
                "Blood Group": convert_blood_group(blood_group),
                "Pulse rate(bpm) ": pulse_rate,
                "Weight gain(Y/N)": convert_yes_no(weight_gain),
                "hair growth(Y/N)": convert_yes_no(hair_growth),
                "Skin darkening (Y/N)": convert_yes_no(skin_darkening),
                "Hair loss(Y/N)": convert_yes_no(hair_loss),
                "Pimples(Y/N)": convert_yes_no(pimples),
                "Fast food (Y/N)": convert_yes_no(fast_food),
                "Reg.Exercise(Y/N)": convert_yes_no(reg_exercise),
                "RR (breaths/min)": rr_rate,
                "Cycle(R/I)": convert_cycle(cycle),
                "Cycle length(days)": cycle_length,
                "Marraige Status (Yrs)": marriage_years,
                "Pregnant(Y/N)": convert_yes_no(pregnancy_status),
                "No. of aborptions": no_of_abortions,
                "Hip(inch)": hip,
                "Waist(inch)": waist,
                "Waist:Hip Ratio": waist_hip_ratio,
                "BP _Systolic (mmHg)": bp_systolic,
                "BP _Diastolic (mmHg)": bp_diastolic
            }
            
            st.json(data)

        try:
            prediction = get_prediction(data)
            st.write(f"Prediction: {prediction}")
        except Exception as e:
            st.error(f"Failed to get prediction: {str(e)}")

        st.session_state.risk_assessment_data = {
            "predicted_pcos": prediction,
            "symptom_analysis": data  
        }

        # st.switch_page("results.py") 
