# import streamlit as st
# import os
# from PIL import Image

# logo_path = "images/logo.png"
# hero_image_path = "images/hero.png"

# feature_images = {
#     "info": "images/info.png",
#     "assessment": "images/assessment.png",
#     "enhanced": "images/enhanced.png",
#     "results": "images/results.png"
# }

# def load_and_resize_image(image_path, size=(150, 150)):
#     """Load an image and resize it to a fixed size."""
#     if os.path.exists(image_path):
#         image = Image.open(image_path)
#         image = image.resize(size)  # Resize to fixed dimensions
#         return image
#     else:
#         return None  # Return None if the image does not exist

# def home_page():
#     # Layout for logo and title
#     col1, col2 = st.columns([1, 4]) 

#     with col1:
#         if os.path.exists(logo_path):
#             st.image(logo_path, width=100)  
#         else:
#             st.error("Logo image not found.")

#     with col2:
#         st.title("PCOS Care")

#     # Welcome Message
#     st.markdown(
#         "<h2 style='text-align: center; color: #6a0dad;'>Empowering Women’s Health with AI-Driven Insights!</h2>", 
#         unsafe_allow_html=True
#     )

#     # Introduction
#     st.markdown("""
#         ### Welcome to PCOS Care  
#         Our AI-driven **PCOS Risk Assessment tool** helps women understand their health better through data-driven insights.  
#         This tool **does not provide a medical diagnosis**, but it serves as an informative resource.  
        
#         💡 **Early detection and awareness are key to managing PCOS effectively.** 
        
#         📌 **Use this platform to assess your risk, gain knowledge, and take informed actions.**  
        
#         _Always consult a healthcare professional for medical advice._  
#     """)

#     # Call to Action
#     st.markdown("<h3 style='text-align: center;'>Start your journey towards better health!</h3>", unsafe_allow_html=True)

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("📚 Learn More About PCOS"):
#             st.session_state.page = "PCOS Information"

#     with col2:
#         if st.button("⚠️ Take the Risk Assessment"):
#             st.session_state.page = "Simple Risk Assessment"

#     # Hero Image
#     st.markdown("<br>", unsafe_allow_html=True)
#     if os.path.exists(hero_image_path):
#         st.image(hero_image_path, use_column_width=True, caption="Take Control of Your Health")
#     else:
#         st.error("Hero image not found.")

#     st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)

#     # Features Overview Section
#     st.subheader("🔎 Overview of the Features")

#     col1, col2, col3, col4 = st.columns(4)

#     # Define a uniform height for the expanders
#     expander_height_style = "min-height: 140px; padding: 10px; text-align: center;"

#     with col1:
#         img = load_and_resize_image(feature_images["info"])
#         if img:
#             st.image(img, caption="PCOS Information", use_column_width=True)
#         with st.expander("📚 PCOS Information"):
#             st.markdown(f"<div style='{expander_height_style}'>Learn about the symptoms, causes, and management strategies.</div>", unsafe_allow_html=True)

#     with col2:
#         img = load_and_resize_image(feature_images["assessment"])
#         if img:
#             st.image(img, caption="Simple Risk Assessment", use_column_width=True)
#         with st.expander("⚠️ Simple Risk Assessment"):
#             st.markdown(f"<div style='{expander_height_style}'>Quickly assess your risk based on key symptoms.</div>", unsafe_allow_html=True)

#     with col3:
#         img = load_and_resize_image(feature_images["enhanced"])
#         if img:
#             st.image(img, caption="Enhanced Risk Assessment", use_column_width=True)
#         with st.expander("🔍 Enhanced Risk Assessment"):
#             st.markdown(f"<div style='{expander_height_style}'>Provide more detailed health data for an in-depth risk evaluation.</div>", unsafe_allow_html=True)

#     with col4:
#         img = load_and_resize_image(feature_images["results"])
#         if img:
#             st.image(img, caption="Results Visualization", use_column_width=True)
#         with st.expander("📊 Results Visualization"):
#             st.markdown(f"<div style='{expander_height_style}'>View your risk level with intuitive graphs and visualizations.</div>", unsafe_allow_html=True)

import streamlit as st
import os
from PIL import Image
from pathlib import Path

# Define image paths
BASE_DIR = Path(__file__).parent  # Get the base directory of the script
IMAGE_DIR = BASE_DIR / "images"   # Define image folder path

logo_path = IMAGE_DIR / "logo.png"
hero_image_path = IMAGE_DIR / "hero.png"

feature_images = {
    "info": IMAGE_DIR / "info.png",
    "assessment": IMAGE_DIR / "assessment.png",
    "enhanced": IMAGE_DIR / "enhanced.png",
    "results": IMAGE_DIR / "results.png"
}

# Function to check and load images
def load_and_resize_image(image_path, size=(150, 150)):
    """Load an image and resize it to a fixed size."""
    if image_path.exists():  # Check if the file exists
        image = Image.open(image_path)
        image = image.resize(size)  # Resize to fixed dimensions
        return image
    else:
        return None  # Return None if the image does not exist

def home_page():
    # Layout for logo and title
    col1, col2 = st.columns([1, 4]) 

    with col1:
        if logo_path.exists():
            st.image(str(logo_path), width=100)  # Convert Path to string
        else:
            st.error("🚨 Logo image not found. Please check the 'images/' folder.")

    with col2:
        st.title("PCOS Care")

    # Welcome Message
    st.markdown(
        "<h2 style='text-align: center; color: #6a0dad;'>Empowering Women’s Health with AI-Driven Insights!</h2>", 
        unsafe_allow_html=True
    )

    # Introduction
    st.markdown("""
        ### Welcome to PCOS Care  
        Our AI-driven **PCOS Risk Assessment tool** helps women understand their health better through data-driven insights.  
        This tool **does not provide a medical diagnosis**, but it serves as an informative resource.  
        
        💡 **Early detection and awareness are key to managing PCOS effectively.** 
        
        📌 **Use this platform to assess your risk, gain knowledge, and take informed actions.**  
        
        _Always consult a healthcare professional for medical advice._  
    """)

    # Call to Action
    st.markdown("<h3 style='text-align: center;'>Start your journey towards better health!</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 Learn More About PCOS"):
            st.session_state.page = "PCOS Information"

    with col2:
        if st.button("⚠️ Take the Risk Assessment"):
            st.session_state.page = "Simple Risk Assessment"

    # Hero Image
    st.markdown("<br>", unsafe_allow_html=True)
    if hero_image_path.exists():
        st.image(str(hero_image_path), use_column_width=True, caption="Take Control of Your Health")
    else:
        st.error("🚨 Hero image not found. Please check the 'images/' folder.")

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
        else:
            st.error("🚨 PCOS Information image missing.")
        with st.expander("📚 PCOS Information"):
            st.markdown(f"<div style='{expander_height_style}'>Learn about the symptoms, causes, and management strategies.</div>", unsafe_allow_html=True)

    with col2:
        img = load_and_resize_image(feature_images["assessment"])
        if img:
            st.image(img, caption="Simple Risk Assessment", use_column_width=True)
        else:
            st.error("🚨 Simple Risk Assessment image missing.")
        with st.expander("⚠️ Simple Risk Assessment"):
            st.markdown(f"<div style='{expander_height_style}'>Quickly assess your risk based on key symptoms.</div>", unsafe_allow_html=True)

    with col3:
        img = load_and_resize_image(feature_images["enhanced"])
        if img:
            st.image(img, caption="Enhanced Risk Assessment", use_column_width=True)
        else:
            st.error("🚨 Enhanced Risk Assessment image missing.")
        with st.expander("🔍 Enhanced Risk Assessment"):
            st.markdown(f"<div style='{expander_height_style}'>Provide more detailed health data for an in-depth risk evaluation.</div>", unsafe_allow_html=True)

    with col4:
        img = load_and_resize_image(feature_images["results"])
        if img:
            st.image(img, caption="Results Visualization", use_column_width=True)
        else:
            st.error("🚨 Results Visualization image missing.")
        with st.expander("📊 Results Visualization"):
            st.markdown(f"<div style='{expander_height_style}'>View your risk level with intuitive graphs and visualizations.</div>", unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    home_page()
