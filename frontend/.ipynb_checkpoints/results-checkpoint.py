import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go  # For gauge charts
import altair as alt  # For bar charts
import numpy as np

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

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
    # Layout for logo and title
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")
        

    st.subheader("Your PCOS Risk Assessment Results")
    st.markdown("<br>", unsafe_allow_html=True)

    # Ensure risk assessment data is available
    if "risk_assessment_data" in st.session_state:
        user_data = st.session_state.risk_assessment_data
        
        # ML-based prediction: Yes or No 
        predicted_pcos = user_data.get("predicted_pcos", "Unknown")  # result from assessment
        
        # Display Prediction
        st.markdown(f"""
            <h3 style='text-align: center; color: #6a0dad;'>Prediction: {predicted_pcos}</h3>  
        """, unsafe_allow_html=True)

        if predicted_pcos == "You are likely to have PCOS":
            custom_alert("This suggests a possibility of PCOS. Please consult a healthcare professional.", "#5A9")   # Greenish-blue
        else:
            custom_alert("No PCOS detected. However, if symptoms persist, consider consulting a doctor.", "#5A9")   # Greenish-blue


        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

        st.subheader("Insights gathered from your data")

        # **1. Ratio-Based Visuals (BMI, Waist-Hip Ratio, FSH/LH)**
        st.subheader("Key Health Ratios")

        bmi = user_data["symptom_analysis"].get("BMI")
        waist_hip_ratio = user_data["symptom_analysis"].get("Waist:Hip Ratio")
        fsh_lh_ratio = user_data["symptom_analysis"].get("FSH/LH")

        col1, col2, col3 = st.columns(3)
        if fsh_lh_ratio is not None:
            with col1:
                st.plotly_chart(create_gauge(bmi, "BMI", 10, 50, "green" if bmi < 25 else "red"))
                custom_alert("A Body Mass Index (BMI) of over 25 may indicate a risk factor for PCOS.", "#5A9")   # Greenish-blue
                
            with col2:
                st.plotly_chart(create_gauge(waist_hip_ratio, "Waist:Hip Ratio", 0.4, 1.0, "green" if waist_hip_ratio < 0.85 else "red"))
                custom_alert("A ratio above 0.85 may indicate a pattern associated with hormonal imbalance.", "#5A9")   # Greenish-blue

            with col3:
                st.plotly_chart(create_gauge(fsh_lh_ratio, "FSH/LH", 0, 3, "red" if fsh_lh_ratio <= 1 else "green"))
                custom_alert("A higher LH than FSH may indicate hormonal imbalance, a key PCOS marker.", "#5A9")   # Greenish-blue

        else:
            with col1:
                if bmi is not None:
                    st.plotly_chart(create_gauge(bmi, "BMI", 10, 50, "green" if bmi < 25 else "red"))
                    custom_alert("A BMI over 25 may indicate a risk factor for PCOS.", "#5A9")   # Greenish-blue
                else:
                    st.markdown("BMI data unavailable")
                    
            
            with col3:
                if waist_hip_ratio is not None:
                    st.plotly_chart(create_gauge(waist_hip_ratio, "Waist:Hip Ratio", 0.4, 1.0, "green" if waist_hip_ratio < 0.85 else "red"))
                    custom_alert("A ratio above 0.85 may indicate a pattern associated with hormonal imbalance.", "#5A9")   # Greenish-blue
                else:
                    st.markdown("Waist-Hip Ratio data unavailable")
                    

        st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
        
        # Adding the overall message
        custom_alert("While your key health ratios show patterns that are sometimes associated with hormonal imbalance, they do not confirm PCOS on their own. It’s always best to consult a healthcare professional for a comprehensive evaluation.", "#5A9")   # Greenish-blue


        # **2. Cycle Irregularities (If Selected)**
        cycle = user_data["symptom_analysis"].get("Cycle(R/I)")
        if cycle == 4:  # Assuming 4 means Irregular
            st.subheader("Cycle Irregularities")
            
            custom_alert("Irregular cycles are commonly associated with PCOS due to hormonal imbalances.", "#5A9")   # Greenish-blue
            
            # Retrieve FSH and LH values
            fsh = float(user_data["symptom_analysis"].get("FSH(mIU/mL)", 0))
            lh = float(user_data["symptom_analysis"].get("LH(mIU/mL)", 0))
        
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
        
            st.altair_chart(chart, use_container_width=True)
        
            # Display additional information based on LH/FSH ratio
            if lh > fsh:
                custom_alert("Your LH is higher than FSH, which could indicate a hormonal imbalance often associated with PCOS. High LH relative to FSH can lead to anovulation (lack of ovulation). Consider discussing these findings with your healthcare provider.", "#5A9")   # Greenish-blue
            elif lh == fsh:
                custom_alert("Your LH and FSH levels are similar. It's important to evaluate other hormonal and clinical factors to get a clearer picture of your health.", "#5A9")   # Greenish-blue
            else:
                custom_alert("Your FSH is higher than LH, which is generally considered more typical. However, it’s still important to monitor your cycle and overall health.", "#5A9")   # Greenish-blue


        # **3. Lifestyle Factors (Weight Gain, Fast Food, No Exercise)**
        weight_gain = user_data["symptom_analysis"].get("Weight gain(Y/N)", 0)
        fast_food = user_data["symptom_analysis"].get("Fast food (Y/N)", 0)
        reg_exercise = user_data["symptom_analysis"].get("Reg.Exercise(Y/N)", 1)

        if weight_gain == 1 or fast_food == 1 or reg_exercise == 0:
            st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
            st.subheader("Lifestyle Factors")
            
            custom_alert("Lifestyle factors can significantly impact PCOS risk.", "#5A9")   # Greenish-blue
            
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
            custom_alert("We strongly recommend seeking medical advice for further evaluation.You can download your data as a PDF to share with your healthcare provider.", "#5A9")   # Greenish-blue
        else:
            custom_alert("Maintain a healthy lifestyle and monitor symptoms over time.", "#5A9")   # Greenish-blue

        st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing
        
        # Disclaimer Section
        st.markdown("""
            <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>
                <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
                <ul style='list-style-type: disc; padding-left: 20px;'>
                    <li>The prediction given on this platform is based on a dataset of <strong>541 patients from Kerala, India</strong>.</li>
                    <li><strong>This is not a medical diagnosis.</strong> It is similar to a preliminary assessment and should not be used as a substitute for clinical evaluation.</li>
                    <li>The accuracy of predictions is <strong>limited by the dataset's scope and quality</strong>, and results may not generalize to all populations.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <p><em>Data from a sample of 541 PCOS patients in Kerala.</em></p>
        <p><a href='https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos' target='_blank'>Source Link</a></p>
        </div>
    """, unsafe_allow_html=True)

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    else:
        custom_alert("No assessment data found. Please complete the assessment first.", "#5A9")   # Greenish-blue

        # Section Break
        st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Call to Action
    st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Explore More</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    # Place the buttons in the center column
    with col1:
        if st.button("Learn More About PCOS"):
            st.session_state.page = "PCOS Information"
        
    with col2:    
        if st.button("Take the Simple Risk Assessment"):
            st.session_state.page = "Simple Risk Assessment"

    with col3:    
        if st.button("Take the Enhanced Risk Assessment"):
            st.session_state.page = "Enhanced Risk Assessment"  

    # st.markdown("TO ADD - disclaimer, references")
