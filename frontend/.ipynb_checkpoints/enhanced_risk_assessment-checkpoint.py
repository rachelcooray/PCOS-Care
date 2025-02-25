import streamlit as st
import os
import requests
import json

# Function to send data to Flask API and get prediction
def get_prediction(input_data):
    # url = "http://127.0.0.1:5000/predict-enhanced"  # Flask API endpoint - localhost
    url = "https://pcos-care.onrender.com/predict-enhanced" # render
    # url = "https://rachelcooray.pythonanywhere.com/predict-enhanced"
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

def validate_cycle(cycle):
    return cycle in ["R", "I"]

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

def validate_beta_hcg_1(value):
    return is_valid_number(value, 0, 1000)

def validate_beta_hcg_2(value):
    return is_valid_number(value, 0, 1000)

def validate_fsh(value):
    return is_valid_number(value, 1, 30)

def validate_lh(value):
    return is_valid_number(value, 1, 30)

def validate_fsh_lh_ratio(value):
    return is_valid_number(value, 0.1, 3.0)

def validate_tsh(value):
    return is_valid_number(value, 0.1, 10.0)

def validate_amh(value):
    return is_valid_number(value, 0.1, 10.0)

def validate_prl(value):
    return is_valid_number(value, 0.1, 100.0)

def validate_vit_d3(value):
    return is_valid_number(value, 1, 100)

def validate_prg(value):
    return is_valid_number(value, 0.1, 50.0)

def validate_rbs(value):
    return is_valid_number(value, 50, 300)

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
    
def enhanced_risk_assessment_page():
    col1, col2 = st.columns([1, 4])  

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    st.subheader("Enhanced Risk Assessment")
    st.markdown("""
    Provide more detailed health data and symptoms for an in-depth analysis of your PCOS risk.
    """)
    
    # Section breaker
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Collect user input for simple risk assessment
    st.write("### General Information")
    age = st.text_input(
        "Age (years):", 
        placeholder="Enter your age (e.g., 25, whole number between 18-50)", 
        help="Enter your age as a whole number between 18 and 50."
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
    pulse_rate = st.text_input(
        "Pulse rate(bpm):", 
        placeholder="Enter your pulse rate in bpm (e.g., 72.0)", 
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
        placeholder="Enter your respiratory rate (e.g., 18)", 
        help="Enter your respiratory rate in breaths per minute."
    )
    
    cycle = st.selectbox(
        "Cycle (R/I):", ["R", "I"], 
        help="Select the cycle type (R for regular, I for irregular)."
    )
    
    cycle_length = st.text_input(
        "Cycle length (days):", 
        placeholder="Enter cycle length in days (e.g., 28)", 
        help="Enter the length of your cycle in days."
    )
    
    marriage_years = st.text_input(
        "Marriage Status (Yrs):", 
        placeholder="Enter years of marriage", 
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
        placeholder="Enter number of abortions", 
        help="Enter the number of abortions (if any)."
    )
    
    hip = st.text_input(
        "Hip (inch):", 
        placeholder="Enter your hip measurement in inches", 
        help="Enter the hip measurement in inches."
    )
    
    waist = st.text_input(
        "Waist (inch):", 
        placeholder="Enter your waist measurement in inches", 
        help="Enter the waist measurement in inches."
    )
    
    waist_hip_ratio = st.text_input(
        "Waist:Hip Ratio:", 
        placeholder="Enter your waist to hip ratio (e.g., 0.8)", 
        help="Enter your waist-to-hip ratio."
    )

    hemoglobin = st.text_input(
        "Hemoglobin level",
        placeholder="Enter your hemoglobin level",
        help="Enter your hemoglobin level."
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

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    st.write("### Hormornal Information")

    beta_hcg_1 = st.text_input(
        "Beta-HCG (I) (mIU/mL):",
        placeholder="Enter your Beta-HCG I value (e.g., 25, whole number between 18-50)", 
        help="Beta-HCG (I) should be a whole number between 18 and 50."
    )
    
    beta_hcg_2 = st.text_input(
        "Beta-HCG (II) (mIU/mL):",
        placeholder="Enter your Beta-HCG II value (whole number between 18-50)",
        help="Beta-HCG (II) should be a whole number between 18 and 50."
    )
    
    fsh = st.text_input(
        "FSH (mIU/mL):",
        placeholder="Enter your FSH level (e.g., 5.5)",
        help="Follicle-stimulating hormone level in mIU/mL."
    )
    
    lh = st.text_input(
        "LH (mIU/mL):",
        placeholder="Enter your LH level (e.g., 6.2)",
        help="Luteinizing hormone level in mIU/mL."
    )
    
    fsh_lh_ratio = st.text_input(
        "FSH/LH Ratio:",
        placeholder="Enter your FSH/LH ratio (e.g., 1.2)",
        help="Ratio of FSH to LH."
    )
    
    tsh = st.text_input(
        "TSH (mIU/L):",
        placeholder="Enter your TSH level (e.g., 2.0)",
        help="Thyroid-stimulating hormone level in mIU/L."
    )
    
    amh = st.text_input(
        "AMH (ng/mL):",
        placeholder="Enter your AMH level (e.g., 3.1)",
        help="Anti-Müllerian hormone level in ng/mL."
    )
    
    prl = st.text_input(
        "PRL (ng/mL):",
        placeholder="Enter your PRL level (e.g., 15.5)",
        help="Prolactin level in ng/mL."
    )
    
    vit_d3 = st.text_input(
        "Vit D3 (ng/mL):",
        placeholder="Enter your Vitamin D3 level (e.g., 30)",
        help="Vitamin D3 level in ng/mL."
    )
    
    prg = st.text_input(
        "PRG (ng/mL):",
        placeholder="Enter your Progesterone level (e.g., 10.2)",
        help="Progesterone level in ng/mL."
    )
    
    rbs = st.text_input(
        "RBS (mg/dl):",
        placeholder="Enter your Random Blood Sugar level (e.g., 110)",
        help="Random blood sugar level in mg/dL."
    )
    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)
    
    st.write("### Follicle Information")
    
    follicle_number_left = st.text_input(
        "Follicle Number (Left):",
        placeholder="Enter the follicle count in the left ovary (e.g., 5)",
        help="Total number of follicles in the left ovary."
    )
    
    follicle_number_right = st.text_input(
        "Follicle Number (Right):",
        placeholder="Enter the follicle count in the right ovary (e.g., 6)",
        help="Total number of follicles in the right ovary."
    )
    
    follicle_size_left = st.text_input(
        "Average Follicle Size (Left) (mm):",
        placeholder="Enter average follicle size in the left ovary (e.g., 12.5)",
        help="Average follicle size in the left ovary in mm."
    )
    
    follicle_size_right = st.text_input(
        "Average Follicle Size (Right) (mm):",
        placeholder="Enter average follicle size in the right ovary (e.g., 13.2)",
        help="Average follicle size in the right ovary in mm."
    )
    
    endometrium_thickness = st.text_input(
        "Endometrium Thickness (mm):",
        placeholder="Enter your endometrial thickness (e.g., 8.0)",
        help="Thickness of the endometrial lining in mm."
    )

    
    # Validate inputs
    if st.button("Submit"):
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

        # add the new ones

        # Collect errors
        errors = []
        if not age_valid: errors.append("Age must be between 18 and 75.")
        if not weight_valid: errors.append("Weight must be between 30 and 200 Kg.")
        if not height_valid: errors.append("Height must be between 100 and 250 cm.")
        if not bmi_valid: errors.append("BMI must be between 10 and 50.")
        if not bp_systolic_valid: errors.append("BP systolic must be between 80 and 200 mmHg.")
        if not bp_diastolic_valid: errors.append("BP diastolic must be between 50 and 120 mmHg.")
        if not pulse_rate_valid: errors.append("Pulse rate must be between 40 and 200 bpm.")
        if not rr_valid: errors.append("Respiratory rate must be between 12 and 30 breaths per minute.")
        if not cycle_valid: errors.append("Cycle must be either 'R' (regular) or 'I' (irregular).")
        if not cycle_length_valid: errors.append("Cycle length must be between 21 and 35 days.")
        if not marriage_years_valid: errors.append("Years of marriage must be between 0 and 60.")
        if not no_of_abortions_valid: errors.append("Number of abortions must be between 0 and 10.")
        if not hip_valid: errors.append("Hip measurement must be between 20 and 70 inches.")
        if not waist_valid: errors.append("Waist measurement must be between 20 and 60 inches.")
        if not waist_hip_ratio_valid: errors.append("Waist to hip ratio must be between 0.4 and 1.0.")

        if not validate_beta_hcg_1(beta_hcg_1): errors.append("Beta-HCG (I) must be between 0 and 1000 mIU/mL.")
        if not validate_beta_hcg_2(beta_hcg_2): errors.append("Beta-HCG (II) must be between 0 and 1000 mIU/mL.")
        if not validate_fsh(fsh): errors.append("FSH must be between 1 and 30 mIU/mL.")
        if not validate_lh(lh): errors.append("LH must be between 1 and 30 mIU/mL.")
        if not validate_fsh_lh_ratio(fsh_lh_ratio): errors.append("FSH/LH Ratio must be between 0.1 and 3.0.")
        if not validate_tsh(tsh): errors.append("TSH must be between 0.1 and 10.0 mIU/L.")
        if not validate_amh(amh): errors.append("AMH must be between 0.1 and 10.0 ng/mL.")
        if not validate_prl(prl): errors.append("PRL must be between 0.1 and 100.0 ng/mL.")
        if not validate_vit_d3(vit_d3): errors.append("Vit D3 must be between 1 and 100 ng/mL.")
        if not validate_prg(prg): errors.append("PRG must be between 0.1 and 50.0 ng/mL.")
        if not validate_rbs(rbs): errors.append("RBS must be between 50 and 300 mg/dl.")
        if not validate_follicle_number(follicle_number_left): errors.append("Follicle Number (Left) must be between 1 and 50.")
        if not validate_follicle_number(follicle_number_right): errors.append("Follicle Number (Right) must be between 1 and 50.")
        if not validate_follicle_size(follicle_size_left): errors.append("Average Follicle Size (Left) must be between 1 and 50 mm.")
        if not validate_follicle_size(follicle_size_right): errors.append("Average Follicle Size (Right) must be between 1 and 50 mm.")
        if not validate_endometrium_thickness(endometrium_thickness): errors.append("Endometrium Thickness must be between 1 and 20 mm.")
        if not validate_hemoglobin(hemoglobin): errors.append("Hemoglobin must be between 5 and 20.")
        

        # add the new ones

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
            
            # st.json(data)

        try:
            prediction = get_prediction(data)
            st.write(f"Prediction: {prediction}")
        except Exception as e:
            st.error(f"Failed to get prediction: {str(e)}")
