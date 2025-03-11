import streamlit as st
import os
from PIL import Image

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")
hero_image_path = os.path.join(current_directory, "images/hero.png")

feature_images = {
    "info": os.path.join(current_directory, "images/info.png"),
    "assessment": os.path.join(current_directory, "images/assessment.png"),
    "enhanced": os.path.join(current_directory, "images/enhanced.png"),
    "results": os.path.join(current_directory, "images/results.png")
}

def load_and_resize_image(image_path, size=(150, 150)):
    """Load an image and resize it to a fixed size."""
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize(size)  
        return image
    else:
        return None  

def home_page():
    # Layout for logo and title
    st.markdown("<div style='text-align: center; margin-bottom: 20px;'>", unsafe_allow_html=True)
    if os.path.exists(logo_path):
        logo_image = load_and_resize_image(logo_path, size=(120, 120))
        if logo_image:
            st.image(logo_image, use_column_width=False, caption="", output_format="PNG", width=120)
    else:
        st.error("Logo image not found.")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #6a0dad;'>PCOS Care</h1>", unsafe_allow_html=True)

    # Welcome Message
    st.markdown(
        "<h2 style='text-align: center; color: #6a0dad;'>Empowering Women’s Health with AI-Driven Insights!</h2>", 
        unsafe_allow_html=True
    )

    # Introduction
    st.markdown("""
        <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>
            <h3 style='text-align: center;'>Welcome to PCOS Care</h3>
            <p>Our AI-driven <strong>PCOS Risk Assessment tool</strong> helps women understand their health better through data-driven insights. This tool <strong>does not provide a medical diagnosis</strong>, but it serves as an informative resource.</p>
            <p><strong>Early detection and awareness are key to managing PCOS effectively.</strong></p>
            <p><strong>Use this platform to assess your risk, gain knowledge, and take informed actions.</strong></p>
            <p><em>Always consult a healthcare professional for medical advice.</em></p>
        </div>
    """, unsafe_allow_html=True)

    # Hero Image
    st.markdown("<br>", unsafe_allow_html=True)
    if os.path.exists(hero_image_path):
        st.image(hero_image_path, use_column_width=True, caption="Take Control of Your Health")
    else:
        st.error("Hero image not found.")

    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

    # Features Overview Section
    st.subheader("🔎 Overview of the Features")

    col1, col2, col3, col4 = st.columns(4)

    # Define a uniform height for the expanders
    expander_height_style = "min-height: 140px; padding: 10px; text-align: center;"

    with col1:
        img = load_and_resize_image(feature_images["info"])
        if img:
            st.image(img, caption="PCOS Information", use_column_width=True)
        with st.expander("📚 PCOS Information"):
            st.markdown(f"<div style='{expander_height_style}'>Learn about the symptoms, causes, and management strategies.</div>", unsafe_allow_html=True)

    with col2:
        img = load_and_resize_image(feature_images["assessment"])
        if img:
            st.image(img, caption="Simple Risk Assessment", use_column_width=True)
        with st.expander("⚠️ Simple Risk Assessment"):
            st.markdown(f"<div style='{expander_height_style}'>Quickly assess your risk based on key symptoms.</div>", unsafe_allow_html=True)

    with col3:
        img = load_and_resize_image(feature_images["enhanced"])
        if img:
            st.image(img, caption="Enhanced Risk Assessment", use_column_width=True)
        with st.expander("🔍 Enhanced Risk Assessment"):
            st.markdown(f"<div style='{expander_height_style}'>Provide more detailed health data for an in-depth risk evaluation.</div>", unsafe_allow_html=True)

    with col4:
        img = load_and_resize_image(feature_images["results"])
        if img:
            st.image(img, caption="Results Visualization", use_column_width=True)
        with st.expander("📊 Results Visualization"):
            st.markdown(f"<div style='{expander_height_style}'>View your risk level with intuitive graphs and visualizations.</div>", unsafe_allow_html=True)

    # Call to Action
    st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Start your journey towards better health!</h3>", unsafe_allow_html=True)

    # Add space between markdown and button
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical space

    col1, col2, col3 = st.columns([1, 1, 1])

    # Place the buttons in the center column
    with col1:
        if st.button("📚 Learn More About PCOS"):
            st.session_state.page = "PCOS Information"
    
    with col3:    
        if st.button("⚠️ Take the Risk Assessment"):
            st.session_state.page = "Simple Risk Assessment"

    # Disclaimer Section
    st.markdown("### Disclaimer")
    st.info("""
    - The prediction given on this platform is based on a dataset of **541 patients from Kerala, India**.
    - **This is not a medical diagnosis.** It is similar to a preliminary assessment and should not be used as a substitute for clinical evaluation.
    - The accuracy of predictions is **limited by the dataset's scope and quality**, and results may not generalize to all populations.
    """)            
            

# Run the home page function when the script is executed
if __name__ == "__main__":
    home_page()