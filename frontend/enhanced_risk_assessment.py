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
    
def enhanced_risk_assessment_page():
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Risk Assessment Tool")
        
    st.subheader("Enhanced Risk Assessment")
    st.markdown("""
    Provide more detailed health data and symptoms for an in-depth analysis of your PCOS risk.  
    """)

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Collecting user input for enhanced risk assessment
    st.write("### General Information")
    age = st.text_input(
        "Age (years):", 
        placeholder="Enter your age (e.g., 25, whole number between 18-60)", 
        help="Enter your age as a whole number between 18 and 60."
    )
    weight = st.text_input(
        "Weight (Kg):", 
        placeholder="Enter your weight in Kg (e.g., 60.5)", 
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
        placeholder="Enter your blood group",
        help="Select your blood group."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Vital Signs")
    pulse_rate = st.text_input(
        "Pulse Rate (bpm):", 
        placeholder="Enter your pulse rate (e.g., 70)", 
        help="Enter your pulse rate in beats per minute."
    )
    rr_rate = st.text_input(
        "Respiratory Rate (breaths/min):", 
        placeholder="Enter respiratory rate (e.g., 20)", 
        help="Enter your respiratory rate in breaths per minute."
    )
    hb = st.text_input(
        "Hemoglobin (Hb) (g/dl):", 
        placeholder="Enter hemoglobin level (e.g., 14.0)", 
        help="Enter your hemoglobin level in grams per deciliter."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Menstrual Cycle")
    cycle = st.radio(
        "Cycle Regularity (R/I):", 
        ["Regular", "Irregular"], 
        index=None, 
        help="Select your menstrual cycle regularity."
    )
    cycle_length = st.text_input(
        "Cycle Length (days):", 
        placeholder="Enter cycle length in days (e.g., 28)", 
        help="Enter your average menstrual cycle length in days."
    )
    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Other Details")
    marriage_years = st.text_input(
        "Marriage Status (Years):", 
        placeholder="Enter number of years married (e.g., 5)", 
        help="Enter the number of years you have been married."
    )
    pregnant = st.radio(
        "Are you currently pregnant? (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you are currently pregnant."
    )
    no_of_abortions = st.text_input(
        "Number of Abortions:", 
        placeholder="Enter number of abortions (e.g., 1)", 
        help="Enter the number of abortions you've had."
    )
   
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Anthropometric Data")
    hip = st.text_input(
        "Hip (inches):", 
        placeholder="Enter hip measurement in inches (e.g., 36)", 
        help="Enter your hip measurement in inches."
    )
    waist = st.text_input(
        "Waist (inches):", 
        placeholder="Enter waist measurement in inches (e.g., 30)", 
        help="Enter your waist measurement in inches."
    )
    waist_hip_ratio = st.text_input(
        "Waist:Hip Ratio:", 
        placeholder="Enter waist-to-hip ratio (e.g., 0.8)", 
        help="Enter your waist-to-hip ratio."
    )
    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Symptoms")
    weight_gain = st.radio(
        "Weight Gain (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have experienced unusual weight gain."
    )
    hair_growth = st.radio(
        "Excessive Hair Growth (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have noticed excessive hair growth."
    )
    skin_darkening = st.radio(
        "Skin Darkening (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if your skin has darkened."
    )
    hair_loss = st.radio(
        "Hair Loss (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you have experienced hair loss."
    )
    pimples = st.radio(
        "Pimples (Y/N):", 
        ["Yes", "No"],
        index=None, 
        help="Select 'Yes' if you have had frequent pimples."
    )
    fast_food = st.radio(
        "Frequent Fast Food Consumption (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you often consume fast food."
    )
    reg_exercise = st.radio(
        "Regular Exercise (Y/N):", 
        ["Yes", "No"], 
        index=None, 
        help="Select 'Yes' if you exercise regularly."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Blood Pressure")
    bp_systolic = st.text_input(
        "BP Systolic (mmHg):", 
        placeholder="Enter systolic BP (e.g., 120)", 
        help="Enter your systolic blood pressure."
    )
    bp_diastolic = st.text_input(
        "BP Diastolic (mmHg):", 
        placeholder="Enter diastolic BP (e.g., 80)", 
        help="Enter your diastolic blood pressure."
    )

    if st.button("Submit"):
        # individual validations
        errors = []
        
        if not validate_age(age):
            errors.append("Invalid age. Age must be between 18 and 75.")
    
        if not validate_weight(weight):
            errors.append("Invalid weight. Weight must be between 30kg and 200kg.")
    
        if not validate_height(height):
            errors.append("Invalid height. Height must be between 100cm and 250cm.")
    
        if not validate_bmi(bmi):
            errors.append("Invalid BMI. BMI must be between 10 and 50.")
    
        if not validate_bp_systolic(bp_systolic):
            errors.append("Invalid systolic blood pressure. Must be between 80 and 200 mmHg.")
    
        if not validate_bp_diastolic(bp_diastolic):
            errors.append("Invalid diastolic blood pressure. Must be between 50 and 120 mmHg.")
    
        if not validate_pulse_rate(pulse_rate):
            errors.append("Invalid pulse rate. Must be between 40 and 200 bpm.")
    
        if not validate_respiratory_rate(rr_rate):
            errors.append("Invalid respiratory rate. Must be between 12 and 30 breaths per minute.")
    
        if not validate_hemoglobin(hb):
            errors.append("Invalid hemoglobin level. Must be between 8 and 18 g/dl.")
    
        if not validate_cycle_length(cycle_length):
            errors.append("Invalid cycle length. Must be between 21 and 35 days.")
    
        if not validate_marriage_years(marriage_years):
            errors.append("Invalid marriage years. Must be between 0 and 60.")
    
        if not validate_number_of_abortions(no_of_abortions):
            errors.append("Invalid number of abortions. Must be between 0 and 10.")
    
        if not validate_hip(hip):
            errors.append("Invalid hip measurement. Must be between 20 and 70 inches.")
    
        if not validate_waist(waist):
            errors.append("Invalid waist measurement. Must be between 20 and 60 inches.")
    
        if not validate_waist_hip_ratio(waist_hip_ratio):
            errors.append("Invalid waist-to-hip ratio. Must be between 0.4 and 1.0.")
            
    
        # Display validation errors or success
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.success("All inputs are valid!")
            
            st.markdown("#### Collected Data Summary:")
            st.json({
                "Age": age,
                "Weight": weight,
                "Height": height,
                "BMI": bmi,
                "Blood Group": blood_group,
                "Pulse Rate": pulse_rate,
                "Respiratory Rate": rr_rate,
                "Hemoglobin": hb,
                "Cycle Regularity": cycle,
                "Cycle Length": cycle_length,
                "Marriage Years": marriage_years,
                "Pregnant": pregnant,
                "Number of Abortions": no_of_abortions,
                "Hip (inches)": hip,
                "Waist (inches)": waist,
                "Waist:Hip Ratio": waist_hip_ratio,
                "Weight Gain": weight_gain,
                "Excessive Hair Growth": hair_growth,
                "Skin Darkening": skin_darkening,
                "Hair Loss": hair_loss,
                "Pimples": pimples,
                "Fast Food": fast_food,
                "Regular Exercise": reg_exercise,
                "BP Systolic": bp_systolic,
                "BP Diastolic": bp_diastolic
            })