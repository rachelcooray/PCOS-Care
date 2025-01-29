import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt

logo_path = "images/logo.png"

def pcos_info_page():
    
    col1, col2 = st.columns([1, 4])  

    with col1:
        # Display the logo
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        # Display the app title
        st.title("PCOS Information")

    # Section: What is PCOS?
    st.markdown("""
        ## What is PCOS?  
        Polycystic Ovary Syndrome (PCOS) is a **hormonal disorder** that affects women of reproductive age.  
        It can lead to **irregular periods, excessive hair growth, acne, weight gain, and fertility issues**.  
        
        🔬 *PCOS is linked to insulin resistance and hormonal imbalances.*  
    """)

    # PCOS Symptoms
    st.markdown("## Common Symptoms")
    symptoms = [
        "📉 **Irregular menstrual cycles**",
        "⚖️ **Unexplained weight gain**",
        "🔴 **Acne and oily skin**",
        "🧑‍🦰 **Thinning hair or hair loss**",
        "🌪 **Mood swings and fatigue**",
        "⚠️ **Dark patches of skin** (especially around the neck or underarms)"
    ]
    for symptom in symptoms:
        st.markdown(f"- {symptom}")

    # Section: Why Early Detection Matters?
    st.markdown("## Why Early Detection Matters?")
    st.markdown("""
        Early detection and lifestyle changes can **help manage symptoms and prevent long-term complications**.  
        
        🚨 **Without treatment, PCOS can increase the risk of:**  
        - Type 2 **Diabetes**  
        - **Heart Disease** & High Blood Pressure  
        - **Infertility** or Pregnancy Complications  
        - Depression & Anxiety  
        
        _Taking action early helps improve overall health and quality of life._  
    """)

    # Section: How PCOS Affects Health
    st.markdown("## How PCOS Affects Health?")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            PCOS affects multiple systems in the body, leading to:
            - ⚠️ **Hormonal imbalances**  
            - 🍔 **Metabolic issues (insulin resistance, weight gain)**  
            - 💔 **Increased risk of cardiovascular disease**  
            - 🏥 **Complications in pregnancy and fertility**  
        """)
    with col2:
        # Placeholder for an infographic or flowchart
        st.image("images/logo.png", use_column_width=True, caption="PCOS Effects on Health")  

    # Section Break
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Example Chart: PCOS Symptom and Lifestyle Relationship
    st.markdown("### PCOS Symptom and Lifestyle Habit Relationship")

    # Data
    data = {
        "Symptoms": [
            "Weight Gain", "Hair Growth", "Skin Darkening",
            "Hair Loss", "Pimples", "Fast Food", "No Regular Exercise"
        ],
        "Prevalence (%)": [68.36, 57.06, 62.15, 57.63, 69.49, 78.53, 71.18]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    st.bar_chart(df.set_index("Symptoms")["Prevalence (%)"])

    # Plotting with Matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df["Symptoms"], df["Prevalence (%)"], color="skyblue")
    ax.set_title("PCOS Symptom and Lifestyle Habit Relationship", fontsize=14)
    ax.set_xlabel("Symptoms", fontsize=12)
    ax.set_ylabel("Prevalence (%)", fontsize=12)
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout()

    st.pyplot(fig)
    
    st.markdown("""
        *Data from a sample of 177 PCOS patients in Kerala.*  
        📌 [Source Link](https://www.example.com)  
    """)

    # Call to Action
    st.markdown("## Take the Next Step")

    
    if st.button("⚠️ Take the Simple Assessment"):
        st.switch_page("Simple_Risk_Assessment")  # Adjust based on your routing