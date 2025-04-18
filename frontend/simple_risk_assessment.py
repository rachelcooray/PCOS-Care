import streamlit as st
import os
import requests
import json
from fpdf import FPDF
import base64

# Function to convert an image to base64 encoding for embedding in HTML
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to send data to Flask API and get prediction
def get_prediction(input_data):
    # url = "http://127.0.0.1:5000/predict-simple"  # Flask API endpoint - localhost
    url = "https://pcos-care.onrender.com/predict-simple" # Flask API endpoint - Render

    headers = {'Content-Type': 'application/json'}
    
    try:
        # Send POST request with user data in JSON format
        response = requests.post(url, json=input_data, headers=headers)
        
        if response.status_code == 200:
            # Extract prediction from response if successful
            prediction = response.json().get('prediction')
            return prediction
        else:
            # Handle any exceptions during the request
            return f"Error: {response.json().get('error')}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

# Function to show a styled alert box 
def custom_alert(message, color):
    """Creates a custom-styled alert box."""
    st.markdown(f"""
        <div style='padding: 15px; border-radius: 10px; background-color: {color}; color: white; font-weight: bold;'>
            {message}
        </div>
    """, unsafe_allow_html=True)

# Function to create PDF report Version of all data and result
def generate_pdf(data, prediction):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "PCOS Simple Risk Assessment Report", ln=True, align='C')
    pdf.ln(10)
    
    # Section: User Input Data
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, "Your Data:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    
    # Create Table
    col_width = 80  # Column width
    row_height = 7  # Row height
    
    # Convert 'Yes/No' answers from 1/0 to 'Yes'/'No' for display in the PDF
    for key, value in data.items():
        display_value = value
        if isinstance(value, int) and value == 1:
            display_value = "Yes"
        elif isinstance(value, int) and value == 0:
            display_value = "No"
        
        pdf.set_font("Arial", style='B', size=10)
        pdf.cell(col_width, row_height, f"{key}", border=1)
        pdf.set_font("Arial", size=10)
        pdf.cell(col_width, row_height, f"{display_value}", border=1)
        pdf.ln(row_height)
    pdf.ln(5)
    
    # Section: Prediction
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, "Prediction:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", style='B', size=14)
    pdf.set_text_color(255, 0, 0)  # Red color for emphasis
    pdf.cell(200, 10, f"{prediction}", ln=True)
    
    # Disclaimer Section
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.set_text_color(0, 0, 0)  # Reset text color to black
    disclaimer_text = (
        "Disclaimer: The PCOSCare web app provides a prediction based on the data you entered. "
        "This tool is for informational purposes only and does not provide a medical diagnosis. " 
        "Predictions are generated based on data from a specific patient dataset. "
        "The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor for diagnosis and treatment. "
        "The accuracy of predictions is limited by the dataset's scope and quality, and results may not apply to everyone. "
    )
    pdf.multi_cell(0, 10, disclaimer_text)
    
    # Save PDF
    pdf_file_path = "pcos_simple_assessment_report.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path
    
# Function to allow users to download the generated PDF 
def download_pdf(data, prediction):
    pdf_path = generate_pdf(data, prediction)
    with open(pdf_path, "rb") as file:
        st.download_button(label="Download Report as PDF", data=file, file_name="PCOS_Simple_Risk_Assessment.pdf", mime="application/pdf")


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
    if not weight or not height:  # Check if inputs are empty
        return None
    try:
        weight = float(weight)
        height = float(height)
        return weight / ((height / 100) ** 2)
    except ValueError:
        return None  # Return None if conversion fails

def calculate_waist_hip_ratio(waist, hip):
    if not waist or not hip:
        return None
    try:
        waist = float(waist)
        hip = float(hip)
        return waist / hip
    except ValueError:
        return None

# Function to call the page
def simple_risk_assessment_page():

    # Initialize session state variables if not present
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    # Custom CSS styling
    st.markdown(
        """
        <style>
            /* Apply border to text inputs */
            div[data-baseweb="input"] > div {
                border: 2px solid #CBB2E6 !important; /* Green border */
                border-radius: 5px;
                padding: 5px;
            }
            
            /* Apply border to select box */
            div[data-baseweb="select"] > div {
                border: 2px solid #CBB2E6 !important; /* Green border */
                border-radius: 5px;
            }
    
            /* Apply border to radio buttons */
            div[data-baseweb="radio"] {
                border: 2px solid #CBB2E6 !important;
                padding: 10px;
                border-radius: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
   
    # Logo and Title
    st.markdown(
        f"""
         <div style='text-align: center;'>
            <img src='data:image/png;base64,{get_base64(logo_path)}' width='100'/> 
            <h1>PCOS Care</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Introduction
    st.subheader("Simple Risk Assessment")
    st.markdown("""
    Provide basic health data and symptoms for a quick PCOS risk analysis. This assessment helps you understand your potential risk for PCOS and provides early insights to guide you toward the right next steps. 
    """)
    
    st.subheader("Before You Start")

    st.write("""
        To ensure accurate results, you will need to gather a few health measurements: your pulse rate, respiratory rate and blood pressure (systolic and diastolic). 
        Make sure you're in a calm, seated position, as stress can impact these readings. Once you're ready, follow the steps below to take your measurements:
    """)
    
    # Provide links to guides
    st.markdown("""
    - [How to measure your pulse rate](https://www.bhf.org.uk/informationsupport/tests/checking-your-pulse)
    - [How to measure your respiratory rate](https://keepingmychesthealthy.bdct.nhs.uk/my-respiratory-rate/)
    - [How to measure your blood pressure (systolic and diastolic)](https://www.bloodpressureuk.org/your-blood-pressure/how-to-lower-your-blood-pressure/monitoring-your-blood-pressure-at-home/how-to-measure-your-blood-pressure-at-home/)

    
    Now, enter the details in the fields below. Guidelines have been provided for each field.
""")

    st.markdown("""
        <p><em>Any data you enter in this form is not stored and is only used during your current session for assessment purposes. Once the session ends, all information is automatically discarded.</em></p>
    """, unsafe_allow_html=True)
    
    # Section breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Collect user input for simple risk assessment
    st.write("### General Information")
    age = st.text_input(
        "Age (years):", 
        value=st.session_state.form_data.get("age", ""),
        placeholder="25", 
        help="Enter your age as a whole number between 18 and 55."
    )
    weight = st.text_input(
        "Weight (kg):", 
        value=st.session_state.form_data.get("weight", ""),
        placeholder="60.5", 
        help="Enter your weight in kilograms. Decimals are allowed."
    )
    height = st.text_input(
        "Height (cm):", 
        value=st.session_state.form_data.get("height", ""),
        placeholder="160.5", 
        help="Enter your height in centimeters. Decimals are allowed."
    )
    blood_group = st.selectbox(
        "Blood Group:", 
        ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], 
        index=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"].index(st.session_state.form_data.get("blood_group", "A+")),
        help="Select your blood group."
    )
    pulse_rate = st.text_input(
        "Pulse Rate (bpm):", 
        value=st.session_state.form_data.get("pulse_rate", ""),
        placeholder="72.0", 
        help="Enter your pulse rate in beats per minute. Decimals are allowed."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Ensure session state has initial values
    if "weight_gain" not in st.session_state:
        st.session_state.weight_gain = None
    if "hair_growth" not in st.session_state:
        st.session_state.hair_growth = None
    if "skin_darkening" not in st.session_state:
        st.session_state.skin_darkening = None
    if "hair_loss" not in st.session_state:
        st.session_state.hair_loss = None
    if "pimples" not in st.session_state:
        st.session_state.pimples = None
    if "fast_food" not in st.session_state:
        st.session_state.fast_food = None
    if "reg_exercise" not in st.session_state:
        st.session_state.reg_exercise = None
    
    st.write("### Symptoms")
    
    # Using `index=None` and managing state with `session_state`
    weight_gain = st.radio(
        "Have you experienced unusual or excessive weight gain recently?", 
        ["Yes", "No"], 
        index=None if st.session_state.weight_gain is None else ["Yes", "No"].index(st.session_state.weight_gain),
        help="Select 'Yes' if you have experienced unusual or excessive weight gain recently."
    )
    
    hair_growth = st.radio(
        "Have you observed abnormal or excessive hair growth?", 
        ["Yes", "No"], 
        index=None if st.session_state.hair_growth is None else ["Yes", "No"].index(st.session_state.hair_growth),
        help="Select 'Yes' if you have observed abnormal or excessive hair growth."
    )
    
    skin_darkening = st.radio(
        "Have you experienced any skin darkening?", 
        ["Yes", "No"], 
        index=None if st.session_state.skin_darkening is None else ["Yes", "No"].index(st.session_state.skin_darkening),
        help="Select 'Yes' if you have noticed dark patches on your skin."
    )
    
    hair_loss = st.radio(
        "Have you observed abnormal or excessive hair loss?", 
        ["Yes", "No"], 
        index=None if st.session_state.hair_loss is None else ["Yes", "No"].index(st.session_state.hair_loss),
        help="Select 'Yes' if you have observed abnormal or excessive hair loss."
    )
    
    pimples = st.radio(
        "Do you have frequent or severe acne outbreaks?", 
        ["Yes", "No"], 
        index=None if st.session_state.pimples is None else ["Yes", "No"].index(st.session_state.pimples),
        help="Select 'Yes' if you have frequent or severe acne outbreaks."
    )
    
    fast_food = st.radio(
        "Do you eat a lot of fast food?", 
        ["Yes", "No"], 
        index=None if st.session_state.fast_food is None else ["Yes", "No"].index(st.session_state.fast_food),
        help="Select 'Yes' if you eat a lot of fast food."
    )
    
    reg_exercise = st.radio(
        "Do you exercise regularly?", 
        ["Yes", "No"], 
        index=None if st.session_state.reg_exercise is None else ["Yes", "No"].index(st.session_state.reg_exercise),
        help="Select 'Yes' if you exercise regularly (at least 3 times a week)."
    )
    
    # Update session state with the selected values
    st.session_state.weight_gain = weight_gain
    st.session_state.hair_growth = hair_growth
    st.session_state.skin_darkening = skin_darkening
    st.session_state.hair_loss = hair_loss
    st.session_state.pimples = pimples
    st.session_state.fast_food = fast_food
    st.session_state.reg_exercise = reg_exercise

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Additional Information")
    
    rr_rate = st.text_input(
        "Respiratory Rate (breaths/min):", 
        value=st.session_state.form_data.get("rr_rate", ""),
        placeholder="18", 
        help="Enter your respiratory rate in breaths per minute. Typical adult respiratory rate is between 12–20 breaths per minute. Count how many times you breathe in 1 minute."
    )
    
    cycle = st.selectbox(
        "Cycle Regularity:", 
        ["Regular", "Irregular"], 
        index=["Regular", "Irregular"].index(st.session_state.form_data.get("cycle", "Regular")),
        help="Select the cycle type as regular or irregular."
    )
    
    cycle_length = st.text_input(
        "Cycle length (days):", 
        value=st.session_state.form_data.get("cycle_length", ""),
        placeholder="7", 
        help="Enter the number of days your menstrual period typically lasts (not the entire cycle)."
    )

    if "pregnancy_status" not in st.session_state:
        st.session_state.pregnancy_status = None
    
    pregnancy_status = st.radio(
        "Have you ever been pregnant?", 
        ["Yes", "No"], 
        index=None if st.session_state.pregnancy_status is None else ["Yes", "No"].index(st.session_state.pregnancy_status),
        help="Select if pregnant (Y) or not (N)."
    )

    st.session_state.pregnancy_status = pregnancy_status

    no_of_abortions = st.text_input(
        "No. of Abortions:", 
        value=st.session_state.form_data.get("no_of_abortions", ""),
        placeholder="0", 
        help="Enter the number of abortions (if any)."
    )
    
    hip = st.text_input(
        "Hip (inch):", 
        value=st.session_state.form_data.get("hip", ""),
        placeholder="36", 
        help="Enter the hip measurement in inches."
    )
    
    waist = st.text_input(
        "Waist (inch):", 
        value=st.session_state.form_data.get("waist", ""),
        placeholder="32", 
        help="Enter the waist measurement in inches."
    )

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Blood Pressure")
    bp_systolic = st.text_input(
        "Systolic Blood Pressure (mmHg):", 
        value=st.session_state.form_data.get("bp_systolic", ""),
        placeholder="120", 
        help="Enter your systolic blood pressure as a whole number between 80 and 200. Systolic is the top number of your blood pressure reading, measured when the heart beats."
    )
    
    bp_diastolic = st.text_input(
        "Diastolic Blood Pressure (mmHg):", 
        value=st.session_state.form_data.get("bp_diastolic", ""),
        placeholder="80", 
        help="Enter your diastolic blood pressure as a whole number between 50 and 120. Diastolic is the bottom number of your blood pressure reading, measured between heartbeats."
    )

    # Save the form data to session state
    st.session_state.form_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "blood_group": blood_group,
        "pulse_rate": pulse_rate,
        "weight_gain": weight_gain,
        "hair_growth": hair_growth,
        "skin_darkening": skin_darkening,
        "hair_loss": hair_loss,
        "pimples": pimples,
        "fast_food": fast_food,
        "reg_exercise": reg_exercise,
        "rr_rate": rr_rate,
        "cycle": cycle,
        "cycle_length": cycle_length,
        "pregnancy_status": pregnancy_status,
        "no_of_abortions": no_of_abortions,
        "hip": hip,
        "waist": waist,
        "bp_systolic": bp_systolic,
        "bp_diastolic": bp_diastolic
    }

    
    # Validate inputs
    if st.button("Submit"):
        with st.spinner("Processing your results..."):
            bmi = None
            waist_hip_ratio = None
    
            if weight and height:
                bmi = calculate_bmi(weight, height)  
            else:
                custom_alert("Weight and Height are required and must be numeric.", "#F0A693")   
                st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
                    
            if waist and hip:
                waist_hip_ratio = calculate_waist_hip_ratio(waist, hip)
            else:
                custom_alert("Waist and Hip measurements are required and must be numeric.", "#F0A693")   
                st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
        
            age_valid = validate_age(age)
            weight_valid = validate_weight(weight)
            height_valid = validate_height(height)
            bmi_valid = validate_bmi(bmi) if bmi else False
            bp_systolic_valid = validate_bp_systolic(bp_systolic)
            bp_diastolic_valid = validate_bp_diastolic(bp_diastolic)
            pulse_rate_valid = validate_pulse_rate(pulse_rate)
            rr_valid = validate_respiratory_rate(rr_rate)
            cycle_valid = validate_cycle(cycle)
            cycle_length_valid = validate_cycle_length(cycle_length)
            no_of_abortions_valid = validate_number_of_abortions(no_of_abortions)
            hip_valid = validate_hip(hip)
            waist_valid = validate_waist(waist)
            waist_hip_ratio_valid = validate_waist_hip_ratio(waist_hip_ratio) if waist_hip_ratio else False
    
            # Collect errors
            errors = []
            if not age_valid: errors.append("Age must be between 18 and 55.")
            if not weight_valid: errors.append("Weight must be between 30 and 200 Kg.")
            if not height_valid: errors.append("Height must be between 90 and 250 cm.")
            if not bp_systolic_valid: errors.append("BP systolic must be between 80 and 200 mmHg.")
            if not bp_diastolic_valid: errors.append("BP diastolic must be between 50 and 120 mmHg.")
            if not pulse_rate_valid: errors.append("Pulse rate must be between 15 and 120 bpm.")
            if not rr_valid: errors.append("Respiratory rate must be between 12 and 30 breaths per minute.")
            if not cycle_valid: errors.append("Cycle must be either 'Regular' or 'Irregular'.")
            if not cycle_length_valid: errors.append("Cycle length must be between 0 and 14 days.")
            if not no_of_abortions_valid: errors.append("Number of abortions must be between 0 and 5.")
            if not hip_valid: errors.append("Hip measurement must be between 20 and 60 inches.")
            if not waist_valid: errors.append("Waist measurement must be between 20 and 55 inches.")
             
            # Show errors if any
            if errors:
                for error in errors:
                    # st.error(error)
                    custom_alert(error, "#F0A693")   
                    st.markdown("<br>", unsafe_allow_html=True)  
            else:
                custom_alert("All inputs are valid! Form submitted successfully.", "#51A199")   
                st.markdown("<br>", unsafe_allow_html=True)  

                # Data for prediction and reporting
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
                    "Pregnant(Y/N)": convert_yes_no(pregnancy_status),
                    "No. of aborptions": no_of_abortions,
                    "Hip(inch)": hip,
                    "Waist(inch)": waist,
                    "Waist:Hip Ratio": waist_hip_ratio,
                    "BP _Systolic (mmHg)": bp_systolic,
                    "BP _Diastolic (mmHg)": bp_diastolic
                }
                
                # st.markdown("TO REMOVE - for testing purposes")
                # st.json(data)
    
            try:
                # Make prediction using model function
                prediction = get_prediction(data)
                
                # st.markdown("TO REMOVE - for testing purposes")
                # st.write(f"Prediction: {prediction}")

                # Save result in session state to persist across pages
                st.session_state.risk_assessment_data = {
                    "predicted_pcos": prediction,
                    "symptom_analysis": data  
                }

                # Generate and offer a PDF download 
                download_pdf(data, prediction)

                # st.markdown("TO REMOVE - for testing purposes")
                # st.session_state.page = "Your Results"

            # Error handling
            except Exception as e:
                custom_alert("Please enter your correct details and try again.", "#51A199")   

    st.write("Please go to the Results page to view detailed insights.")