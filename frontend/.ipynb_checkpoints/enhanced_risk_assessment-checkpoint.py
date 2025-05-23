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
    # url = "http://127.0.0.1:5000/predict-enhanced"  # Flask API endpoint - localhost
    url = "https://pcos-care.onrender.com/predict-enhanced" # Flask API endpoint - Render
    
    headers = {'Content-Type': 'application/json'}
    
    try:
        # Send POST request with user data in JSON format
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
    pdf.cell(200, 10, "PCOS Enhanced Risk Assessment Report", ln=True, align='C')
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
        st.download_button(label="Download Report as PDF", data=file, file_name="PCOS_Enhanced_Risk_Assessment.pdf", mime="application/pdf")

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
    return is_valid_number(hb, 5, 20)

def validate_cycle(cycle):
    return cycle in ["Regular", "Irregular"]

def validate_cycle_length(cycle_length):
    return is_valid_number(cycle_length, 0, 14)

def validate_number_of_abortions(no_of_abortions):
    return is_valid_number(no_of_abortions, 0, 55)

def validate_hip(hip):
    return is_valid_number(hip, 20, 70)

def validate_waist(waist):
    return is_valid_number(waist, 20, 60)

def validate_waist_hip_ratio(waist_hip_ratio):
    return is_valid_number(waist_hip_ratio, 0.4, 1.0)

def validate_beta_hcg_1(value):
    return is_valid_number(value, 0, 35000)

def validate_beta_hcg_2(value):
    return is_valid_number(value, 0, 30000)

def validate_fsh(value):
    return is_valid_number(value, 0, 5000)

def validate_lh(value):
    return is_valid_number(value, 0, 2500)

def validate_fsh_lh_ratio(value):
    return is_valid_number(value, 0, 1500)

def validate_tsh(value):
    return is_valid_number(value, 0.0, 70.0)

def validate_amh(value):
    return is_valid_number(value, 0.0, 70.0)

def validate_prl(value):
    return is_valid_number(value, 0.0, 130.0)

def validate_vit_d3(value):
    return is_valid_number(value, 1, 6500)

def validate_prg(value):
    return is_valid_number(value, 0.1, 90.0)

def validate_rbs(value):
    return is_valid_number(value, 50, 400)

def validate_follicle_number(value):
    return is_valid_number(value, 1, 50)

def validate_follicle_size(value):
    return is_valid_number(value, 1, 50)

def validate_endometrium_thickness(value):
    return is_valid_number(value, 1, 20)

def convert_yes_no(value):
    return 1 if value == "Yes" else 0

def convert_cycle(value):
    return 2 if value == "R" else 4

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

def calculate_fsh_lh_ratio(fsh, lh):
    fsh = float(fsh)
    lh = float(lh)
    return (fsh / lh)
    
def enhanced_risk_assessment_page():

    # Initialize session state variables if not present
    if "form_data" not in st.session_state:
        st.session_state.form_data = {}

    # CSS Styling
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

    st.subheader("Enhanced Risk Assessment")
    st.markdown("""
    Provide more detailed health data and symptoms for an in-depth analysis of your PCOS risk. This form is ideal if you have access to hormonal data from blood tests or abdominal scans. By providing comprehensive information, you can gain a more accurate understanding of your PCOS risk and receive personalized insights and recommendations.
    
    ### Before You Start
    To ensure accurate results, you will need to gather a few key health measurements: your pulse rate, respiratory rate, and blood pressure (systolic and diastolic). It's essential to be in a calm, seated position, as stress can impact these readings. Once you're ready, follow the steps below to take your measurements:
    
    - [How to measure your pulse rate](https://www.bhf.org.uk/informationsupport/tests/checking-your-pulse)
    - [How to measure your respiratory rate](https://keepingmychesthealthy.bdct.nhs.uk/my-respiratory-rate/)
    - [How to measure your blood pressure (systolic and diastolic)](https://www.bloodpressureuk.org/your-blood-pressure/how-to-lower-your-blood-pressure/monitoring-your-blood-pressure-at-home/how-to-measure-your-blood-pressure-at-home/)
    
    Additionally, you will need to have data from relevant blood tests and scans to gather your hormonal levels, including tests for:
    - **Beta-HCG (Beta-Human Chorionic Gonadotropin)**  
    - **FSH (Follicle-Stimulating Hormone)**  
    - **LH (Luteinizing Hormone)**  
    - **TSH (Thyroid-Stimulating Hormone)**  
    - **AMH (Anti-Müllerian Hormone)**  
    - **PRL (Prolactin)**  
    - **Vitamin D3**  
    - **Progesterone**  
    - **Random Blood Sugar (RBS)**  
    - **Pelvic Ultrasound Scan**  
    
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

    st.write("### Other")
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
    
    hemoglobin = st.text_input(
        "Hemoglobin Level",
        value=st.session_state.form_data.get("hemoglobin", ""),
        placeholder="12", 
        help="Enter your hemoglobin level. Decimals are allowed."
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

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Hormornal Information")

    beta_hcg_1 = st.text_input(
        "Beta-HCG (I) (mIU/mL):",
        value=st.session_state.form_data.get("beta_hcg_1", ""),
        placeholder="25", 
        help="Beta-HCG (Human Chorionic Gonadotropin) is a hormone produced during pregnancy. The (I) refers to the initial measurement, typically done early in pregnancy to confirm pregnancy. Enter your Beta-HCG level in mIU/mL. Decimals are allowed."
    )
    
    beta_hcg_2 = st.text_input(
        "Beta-HCG (II) (mIU/mL):",
        value=st.session_state.form_data.get("beta_hcg_2", ""),
        placeholder="25", 
        help="Beta-HCG (II) refers to a follow-up measurement of the hormone, typically taken a few days or weeks after the initial test to track pregnancy progress. Enter the follow-up Beta-HCG level in mIU/mL. Decimals are allowed."
    )
    
    fsh = st.text_input(
        "Follicle-Stimulating Hormone (FSH) (mIU/mL):",
        value=st.session_state.form_data.get("fsh", ""),
        placeholder="5.5", 
        help="Follicle-Stimulating Hormone (FSH) is a hormone that helps regulate the menstrual cycle and promotes the growth of eggs in the ovaries. Enter the follicle-stimulating hormone level in mIU/mL. Decimals are allowed."
    )
    
    lh = st.text_input(
        "Luteinizing Hormone (LH) (mIU/mL):",
        value=st.session_state.form_data.get("lh", ""),
        placeholder="6.2", 
        help="Luteinizing Hormone (LH) plays a key role in the menstrual cycle and the release of eggs from the ovaries (ovulation). Enter your LH level in mIU/mL. Decimals are allowed."
    )
    
    tsh = st.text_input(
        "Thyroid-Stimulating Hormone (TSH) (mIU/L):",
        value=st.session_state.form_data.get("tsh", ""),
        placeholder="2.0",
        help="Thyroid-Stimulating Hormone (TSH) regulates thyroid function. High or low levels can indicate thyroid disorders. Enter the thyroid-stimulating hormone level in mIU/L. Decimals are allowed."
    )
    
    amh = st.text_input(
        "Anti-Müllerian Hormone (AMH) (ng/mL):",
        value=st.session_state.form_data.get("amh", ""),
        placeholder="3.1",
        help="Anti-Müllerian Hormone (AMH) is a marker of ovarian reserve (the number of eggs remaining in the ovaries). Higher levels usually indicate more eggs. Enter the Anti-Müllerian hormone level in ng/mL. Decimals are allowed."
    )
    
    prl = st.text_input(
        "Prolactin (PRL) (ng/mL):",
        value=st.session_state.form_data.get("prl", ""),
        placeholder="15.5",
        help="Prolactin is a hormone involved in milk production and reproductive health. Elevated levels can affect ovulation. Enter the Prolactin level in ng/mL. Decimals are allowed."
    )
    
    vit_d3 = st.text_input(
        "Vitamin D3 (ng/mL):",
        value=st.session_state.form_data.get("vit_d3", ""),
        placeholder="30",
        help="Vitamin D3 is important for calcium absorption and overall health. Low levels can impact fertility. Enter the Vitamin D3 level in ng/mL. Decimals are allowed."
    )
    
    prg = st.text_input(
        "Progesterone (PRG) (ng/mL):",
        value=st.session_state.form_data.get("prg", ""),
        placeholder="10.2",
        help="Progesterone is a hormone that helps regulate the menstrual cycle and supports pregnancy. Enter the Progesterone level in ng/mL. Decimals are allowed."
    )
    
    rbs = st.text_input(
        "Random Blood Sugar (RBS) (mg/dl):",
        value=st.session_state.form_data.get("rbs", ""),
        placeholder="110",
        help="Random Blood Sugar (RBS) measures your blood sugar levels at any time of the day. Enter the Random Blood Sugar level in mg/dL. Decimals are allowed."
    )
    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)
    
    st.write("### Follicle Information")
    
    follicle_number_left = st.text_input(
        "Follicle Count (Left Ovary):",
        value=st.session_state.form_data.get("follicle_number_left", ""),
        placeholder="5",
        help="Follicles are small sacs in the ovaries that contain eggs. The follicle count indicates the number of follicles in your left ovary. Whole numbers only."
    )
    
    follicle_number_right = st.text_input(
        "Follicle Count (Right Ovary):",
        value=st.session_state.form_data.get("follicle_number_right", ""),
        placeholder="6",
        help="Follicles are small sacs in the ovaries that contain eggs. The follicle count indicates the number of follicles in your right ovary. Whole numbers only."
    )
    
    follicle_size_left = st.text_input(
        "Average Follicle Size (Left) (mm):",
        value=st.session_state.form_data.get("follicle_size_left", ""),
        placeholder="12.5",
        help="Enter the average follicle size in the left ovary in mm. Decimals are allowed. This is typically measured during an ultrasound."
    )
    
    follicle_size_right = st.text_input(
        "Average Follicle Size (Right) (mm):",
        value=st.session_state.form_data.get("follicle_size_right", ""),
        placeholder="13.2",
        help="Enter the average follicle size in the right ovary in mm. Decimals are allowed. This is typically measured during an ultrasound."
    )
    
    endometrium_thickness = st.text_input(
        "Endometrium Thickness (mm):",
        value=st.session_state.form_data.get("endometrium_thickness", ""),
        placeholder="8.0",
        help="Endometrium thickness refers to the thickness of the uterine lining, which thickens during the menstrual cycle in preparation for pregnancy. Enter the thickness of the endometrial lining in mm. Decimals are allowed."
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
        "hemoglobin": hemoglobin,
        "bp_systolic": bp_systolic,
        "bp_diastolic": bp_diastolic,
        "beta_hcg_1": beta_hcg_1,
        "beta_hcg_2": beta_hcg_2,
        "fsh": fsh,
        "lh": lh,
        "tsh": tsh,
        "amh": amh,
        "prl": prl,
        "vit_d3": vit_d3,
        "prg": prg,
        "rbs": rbs,
        "follicle_number_left": follicle_number_left,
        "follicle_number_right": follicle_number_right,
        "follicle_size_left": follicle_size_left,
        "follicle_size_right": follicle_size_right,
        "endometrium_thickness": endometrium_thickness
    }

    # Validate inputs
    if st.button("Submit"):
        with st.spinner("Processing your results..."):
            bmi = None
            waist_hip_ratio = None
            fsh_lh_ratio = None
    
            if weight and height:
                bmi = calculate_bmi(weight, height)  
            else:
                custom_alert("Weight and Height are required and must be numeric.", "#F0A693")   
                st.markdown("<br>", unsafe_allow_html=True)  
            
            if waist and hip:
                waist_hip_ratio = calculate_waist_hip_ratio(waist, hip)
            else:
                custom_alert("Waist and Hip measurements are required and must be numeric.", "#F0A693")   
                st.markdown("<br>", unsafe_allow_html=True)  
    
            if fsh and lh:
                fsh_lh_ratio = calculate_fsh_lh_ratio(fsh, lh)
            else:
                custom_alert("FSH and LH values are required and must be numeric.", "#F0A693")   
                st.markdown("<br>", unsafe_allow_html=True)  
            
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
            fsh_lh_ratio_valid = validate_fsh_lh_ratio(fsh_lh_ratio) if fsh_lh_ratio else False
    
            # Collect errors
            errors = []
            if not age_valid: errors.append("Age must be between 18 and 75.")
            if not weight_valid: errors.append("Weight must be between 30 and 200 kg.")
            if not height_valid: errors.append("Height must be between 100 and 250 cm.")
            if not bp_systolic_valid: errors.append("BP systolic must be between 80 and 200 mmHg.")
            if not bp_diastolic_valid: errors.append("BP diastolic must be between 50 and 120 mmHg.")
            if not pulse_rate_valid: errors.append("Pulse rate must be between 40 and 200 bpm.")
            if not rr_valid: errors.append("Respiratory rate must be between 12 and 30 breaths per minute.")
            if not cycle_valid: errors.append("Cycle must be either 'R' (regular) or 'I' (irregular).")
            if not cycle_length_valid: errors.append("Cycle length must be between 21 and 35 days.")
            if not no_of_abortions_valid: errors.append("Number of abortions must be between 0 and 55.")
            if not hip_valid: errors.append("Hip measurement must be between 20 and 70 inches.")
            if not waist_valid: errors.append("Waist measurement must be between 20 and 60 inches.")
            if not validate_beta_hcg_1(beta_hcg_1): errors.append("Beta-HCG (I) must be between 0 and 35000 mIU/mL.")
            if not validate_beta_hcg_2(beta_hcg_2): errors.append("Beta-HCG (II) must be between 0 and 30000 mIU/mL.")
            if not validate_fsh(fsh): errors.append("FSH must be between 0 and 5000 mIU/mL.")
            if not validate_lh(lh): errors.append("LH must be between 0 and 2500 mIU/mL.")
            if not validate_tsh(tsh): errors.append("TSH must be between 0 and 70 mIU/L.")
            if not validate_amh(amh): errors.append("AMH must be between 0 and 70 ng/mL.")
            if not validate_prl(prl): errors.append("PRL must be between 0 and 130 ng/mL.")
            if not validate_vit_d3(vit_d3): errors.append("Vit D3 must be between 1 and 6500 ng/mL.")
            if not validate_prg(prg): errors.append("PRG must be between 0.0 and 90.0 ng/mL.")
            if not validate_rbs(rbs): errors.append("RBS must be between 50 and 400 mg/dl.")
            if not validate_follicle_number(follicle_number_left): errors.append("Follicle Number (Left) must be between 1 and 50.")
            if not validate_follicle_number(follicle_number_right): errors.append("Follicle Number (Right) must be between 1 and 50.")
            if not validate_follicle_size(follicle_size_left): errors.append("Average Follicle Size (Left) must be between 1 and 50 mm.")
            if not validate_follicle_size(follicle_size_right): errors.append("Average Follicle Size (Right) must be between 1 and 50 mm.")
            if not validate_endometrium_thickness(endometrium_thickness): errors.append("Endometrium Thickness must be between 1 and 20 mm.")
            if not validate_hemoglobin(hemoglobin): errors.append("Hemoglobin must be between 5 and 20.")
    
            # Show errors if any
            if errors:
                for error in errors:
                    custom_alert(error, "#F0A693")   # Greenish-blue
                    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
            else:
                custom_alert("All inputs are valid! Form submitted successfully.", "#5A9")   # Greenish-blue
                st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing

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
                    "BP _Diastolic (mmHg)": bp_diastolic,
                    "  I   beta-HCG(mIU/mL)": beta_hcg_1,
                    "II    beta-HCG(mIU/mL)": beta_hcg_2,
                    "FSH(mIU/mL)": fsh,
                    "LH(mIU/mL)": lh,
                    "FSH/LH": fsh_lh_ratio,
                    "TSH (mIU/L)": tsh,
                    "AMH(ng/mL)": amh,
                    "PRL(ng/mL)": prl,
                    "Vit D3 (ng/mL)": vit_d3,
                    "PRG(ng/mL)": prg,
                    "RBS(mg/dl)": rbs,
                    "Follicle No. (L)": follicle_number_left,
                    "Follicle No. (R)": follicle_number_right,
                    "Avg. F size (L) (mm)": follicle_size_left,
                    "Avg. F size (R) (mm)": follicle_size_right,
                    "Endometrium (mm)": endometrium_thickness,
                    "Hb(g/dl)": hemoglobin
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