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
        st.title("APP NAME")
        
    st.subheader("PCOS Information")
    st.markdown("""
        ### What is PCOS?  
        Polycystic Ovary Syndrome (PCOS) is a hormonal disorder common among women of reproductive age.  
        Symptoms include:
        - Irregular menstrual cycles
        - Excessive hair growth (hirsutism)
        - Acne or oily skin
        - Difficulty in conceiving
    """)

    with st.expander("Learn more about PCOS causes and management strategies"):
        st.markdown("""
            - **Causes**: The exact cause of PCOS is not known, but factors such as genetics, insulin resistance, and inflammation may play a role.
            - **Management**: Lifestyle changes, medications like birth control pills, and insulin-sensitizing drugs are often prescribed to manage symptoms.
        """)

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Symptoms section 
    st.markdown("### Symptoms")
    st.markdown("""
        Common symptoms of PCOS include:
        - Irregular or absent menstrual cycles
        - Excessive hair growth on the face or body (hirsutism)
        - Acne or oily skin
        - Weight gain or difficulty losing weight
        - Thinning hair or hair loss on the scalp
        - Fertility challenges or difficulty conceiving
        - Dark patches of skin, especially around the neck or underarms
        - Fatigue and mood changes
    """)  

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Management tips with expanders
    st.markdown("### Management Tips")
    with st.expander("Lifestyle Changes"):
        st.markdown("""
            - Regular exercise (yoga, strength training).
            - Stress management techniques (meditation, therapy).
            - Prioritize sleep hygiene.
        """)

    with st.expander("Medical Treatments"):
        st.markdown("""
            - Hormonal treatments (birth control pills).
            - Insulin-sensitizing drugs (Metformin).
        """)

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Diet tips section
    st.markdown("### Diet Tips")
    st.markdown("""
        Focus on a balanced diet with low-glycemic-index (GI) foods:
        - **Breakfast**: Oatmeal with nuts and berries.
        - **Lunch**: Grilled chicken with quinoa and steamed vegetables.
        - **Snack**: Greek yogurt with seeds.
        - **Dinner**: Baked salmon with a side of roasted vegetables.
    """)
    st.info("Tip: Avoid processed foods and excessive sugar for better symptom management.")

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Useful resources with links
    st.markdown("### Useful Resources")
    st.markdown("""
        - [PCOS Awareness](https://www.example.com)
        - [Link](https://www.example.com)
        - [Healthy Recipes for PCOS](https://www.example.com)
        - [Link](https://www.example.com)
    """)

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)
    
    # Example Chart
    st.markdown("### PCOS Symptom and Lifestyle Habit Relationship")

    # Data
    data = {
        "Symptoms": [
            "Weight Gain",
            "Hair Growth",
            "Skin Darkening",
            "Hair Loss",
            "Pimples",
            "Fast Food",
            "No Regular Exercise"
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
        *Data from a sample of 177 PCOS patients, in Kerala. add the link.* 
    """)