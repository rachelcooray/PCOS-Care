import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go  # For gauge charts
import altair as alt  # For bar charts
import numpy as np
from fpdf import FPDF
import base64

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

# PDF Version of all data and result
def generate_pdf(data, prediction):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "PCOS Risk Assessment Report", ln=True, align='C')
    pdf.ln(10)
    
    # Section: User Input Data
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, "Your Data:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=10)
    
    # Check for 'symptom_analysis' and 'predicted_pcos' in the data
    if "symptom_analysis" in data:
        symptom_data = data["symptom_analysis"]
        
        # Create Table for symptom analysis
        col_width = 80  # Column width
        row_height = 7  # Row height

        for key, value in symptom_data.items():
            display_value = value
            # Handle 'Yes'/'No' conversions (if the data is 1/0)
            if isinstance(value, int):
                display_value = "Yes" if value == 1 else "No"
            
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
        "Predictions are based on available data from a dataset of patients in Kerala, India. "
        "The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor for diagnosis and treatment. "
        "The accuracy of predictions is limited by the dataset's scope and quality, and results may not apply to everyone. "
    )
    pdf.multi_cell(0, 10, disclaimer_text)
    
    # Save PDF
    pdf_file_path = "pcos_assessment_report.pdf"
    pdf.output(pdf_file_path)
    return pdf_file_path

def download_pdf(data, prediction):
    pdf_path = generate_pdf(data, prediction)
    with open(pdf_path, "rb") as file:
        st.download_button(label="Download Report as PDF", data=file, file_name="PCOS_Risk_Assessment.pdf", mime="application/pdf")


def create_gauge(value, title, min_val, max_val, color="blue"):
    """ Creates a simple gauge chart using Plotly. """
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},
        gauge={'axis': {'range': [min_val, max_val]},
               'bar': {'color': color}}))
    return fig

def custom_alert(message, color):
    """Creates a custom-styled alert box."""
    st.markdown(f"""
        <div style='padding: 15px; border-radius: 10px; background-color: {color}; color: white; font-weight: bold;'>
            {message}
        </div>
    """, unsafe_allow_html=True)

def results_page():
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
        

    st.subheader("Your PCOS Risk Assessment Results")
    st.markdown("<br>", unsafe_allow_html=True)

    # Ensure risk assessment data is available
    if "risk_assessment_data" in st.session_state:
        user_data = st.session_state.risk_assessment_data
        
        # ML-based prediction: Yes or No 
        predicted_pcos = user_data.get("predicted_pcos", "Unknown")  # result from assessment
        
        # Display Prediction
        st.markdown(f"""
            <h3 style='text-align: center; color: #6a0dad;'>Our prediction is that: {predicted_pcos}</h3>  
        """, unsafe_allow_html=True)

        if predicted_pcos == "You are likely to have PCOS":
            custom_alert("This suggests a possibility of having PCOS. Please consult a healthcare professional.", "#E76F51")  
        else:
            custom_alert("No PCOS detected. However, if symptoms persist, consider consulting a doctor.", "#9DC3D2")   


        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        st.markdown("""
            <h3 style='text-align: center;'>Insights gathered from your data</h3>
        """, unsafe_allow_html=True)

        # **1. Ratio-Based Visuals (BMI, Waist-Hip Ratio, FSH/LH)**
        st.subheader("Key Health Ratios")

        bmi = user_data["symptom_analysis"].get("BMI")
        waist_hip_ratio = user_data["symptom_analysis"].get("Waist:Hip Ratio")
        fsh_lh_ratio = user_data["symptom_analysis"].get("FSH/LH")

        col1, col2, col3 = st.columns(3)
        if fsh_lh_ratio is not None:
            with col1:
                st.plotly_chart(create_gauge(bmi, "BMI", 10, 50, "green" if bmi < 25 else "red"))
                custom_alert("A Body Mass Index (BMI) of over 25 may indicate a risk factor for PCOS.", "#9DC3D2")   
                
            with col2:
                st.plotly_chart(create_gauge(waist_hip_ratio, "Waist:Hip Ratio", 0.4, 1.0, "green" if waist_hip_ratio < 0.85 else "red"))
                custom_alert("A ratio above 0.85 may indicate a pattern associated with hormonal imbalance.", "#9DC3D2")   

            with col3:
                st.plotly_chart(create_gauge(fsh_lh_ratio, "FSH/LH", 0, 3, "red" if fsh_lh_ratio <= 1 else "green"))
                custom_alert("A lower FSH than LH may indicate hormonal imbalance, a key PCOS marker.", "#9DC3D2")   

        else:
            with col1:
                if bmi is not None:
                    st.plotly_chart(create_gauge(bmi, "BMI", 10, 50, "green" if bmi < 25 else "red"))
                    custom_alert("A BMI over 25 may indicate a risk factor for PCOS.", "#9DC3D2")   
                else:
                    st.markdown("BMI data unavailable")
                    
            
            with col3:
                if waist_hip_ratio is not None:
                    st.plotly_chart(create_gauge(waist_hip_ratio, "Waist:Hip Ratio", 0.4, 1.0, "green" if waist_hip_ratio < 0.85 else "red"))
                    custom_alert("A ratio above 0.85 may indicate a pattern associated with hormonal imbalance.", "#9DC3D2")   
                else:
                    st.markdown("Waist-Hip Ratio data unavailable")
                    

        st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
        
        # Adding the overall message
        custom_alert("While your key health ratios show patterns that are sometimes associated with hormonal imbalance, they do not confirm PCOS on their own. It’s always best to consult a healthcare professional for a comprehensive evaluation.", "#9F90FA") 

        


        # **2. Cycle Irregularities (If Selected)**
        cycle = user_data["symptom_analysis"].get("Cycle(R/I)")
        if cycle == 4:  # Assuming 4 means Irregular
            st.subheader("Cycle Irregularities")
            
            custom_alert("Irregular cycles are commonly associated with PCOS due to hormonal imbalances such as Follicle-stimulating hormone(FSH) and Luteinizing hormone (LH).", "#5A4CA4")   # Greenish-blue
            
            # Retrieve FSH and LH values
            fsh = float(user_data["symptom_analysis"].get("FSH(mIU/mL)", 0))
            lh = float(user_data["symptom_analysis"].get("LH(mIU/mL)", 0))

            if fsh > 0 and lh > 0:
        
                # Create a DataFrame for Altair
                df = pd.DataFrame({
                    "Hormone": ["FSH (mIU/mL)", "LH (mIU/mL)"],
                    "Value": [fsh, lh]
                })
            
                # Create a slimmer bar chart with Altair
                chart = alt.Chart(df).mark_bar(width=40).encode(
                    x=alt.X("Hormone", sort=None),  # Keeps order as given
                    y="Value",
                    color=alt.Color("Hormone", legend=None)
                ).properties(height=300)

                st.markdown("<br><br>", unsafe_allow_html=True)  # Adds spacing
                st.altair_chart(chart, use_container_width=True)
                st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
            
                # Display additional information based on LH/FSH ratio
                if lh > fsh:
                    custom_alert("Your LH Level is higher than  the FSH Level, which could indicate a hormonal imbalance often associated with PCOS. High LH relative to FSH can lead to anovulation (lack of ovulation). Consider discussing these findings with your healthcare provider.", "#E76F51")   
                elif lh == fsh:
                    custom_alert("Your LH and FSH levels are similar. It's important to evaluate other hormonal and clinical factors to get a clearer picture of your health.", "#F4A261")   # Greenish-blue
                else:
                    custom_alert("Your FSH is higher than LH, which is generally considered more typical. However, it’s still important to monitor your cycle and overall health.", "#9DC3D2")   # Greenish-blue


        # **3. Lifestyle Factors (Weight Gain, Fast Food, No Exercise)**
        weight_gain = user_data["symptom_analysis"].get("Weight gain(Y/N)", 0)
        fast_food = user_data["symptom_analysis"].get("Fast food (Y/N)", 0)
        reg_exercise = user_data["symptom_analysis"].get("Reg.Exercise(Y/N)", 1)

        if weight_gain == 1 or fast_food == 1 or reg_exercise == 0:
            st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
            st.subheader("Lifestyle Factors")
            
            custom_alert("Lifestyle factors can significantly impact PCOS risk.", "#5A4CA4")   
            
            st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
            
            st.info("""
            - **Weight Gain:** Excess weight can worsen insulin resistance, a key PCOS factor.
            - **Fast Food Consumption:** Processed foods may contribute to hormone imbalances.
            - **Lack of Exercise:** Regular physical activity can help regulate hormones.
            """)

        # Next Steps Based on Prediction
        st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
        st.subheader("Next Steps")
        if predicted_pcos == "You are likely to have PCOS":
            custom_alert("We strongly recommend seeking medical advice for further evaluation.You can download your data as a PDF to share with your healthcare provider.", "#5A4CA4")   # Greenish-blue
        else:
            custom_alert("Maintain a healthy lifestyle and monitor symptoms over time.", "#9DC3D2")   

        st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing

        st.subheader("Download your Report:")
        download_pdf(user_data, predicted_pcos)
        
        # Disclaimer Section
        st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are based on available data from a dataset of patients in Kerala, India.</li>
                <li>The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor for diagnosis and treatment.</li>
                <li>The accuracy of predictions is limited by the dataset's scope and quality, and results may not apply to everyone.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

        # st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing

        # st.markdown("""
        #     <p><em>Data from a sample of 541 PCOS patients in Kerala.</em></p>
        #     <p><a href='https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos' target='_blank'>Source Link</a></p>
        #     </div>
        # """, unsafe_allow_html=True)

    else:
        custom_alert("No assessment data found. Please complete the assessment first.", "#5A4CA4")   
