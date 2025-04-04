import streamlit as st
import os
from PIL import Image
import base64

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

def load_and_resize_image(image_path, size=(70, 70)):
    """Load an image and resize it to a fixed size."""
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize(size)  
        return image
    else:
        return None

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


def home_page():
    try:
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

    
        # Welcome Message
        st.markdown(
            "<h2 style='text-align: center; color: #bb8ade;'>Empowering Women’s Health with Technology</h2>", 
            unsafe_allow_html=True
        )
    
        # Introduction
        st.markdown("""
            <div style='background-color: #E9E0F4; padding: 20px; border-radius: 10px;'>
                <h3 style='text-align: center;'>Welcome to PCOS Care</h3>
                <p>Our AI-driven <strong>PCOS Risk Assessment tool</strong> helps women understand their health better with data-driven insights. This tool <strong>does not provide a medical diagnosis</strong>, but it serves as an informative resource.</p>
                <p>Early detection and awareness are key to managing PCOS effectively.</p>
                <p>Use this platform to assess your risk, gain knowledge, and take informed actions.</p>
                <p style='text-align: center;'><strong>Always consult a healthcare professional for medical advice.</strong></p>
            </div>
        """, unsafe_allow_html=True)
    
        # Image Section with Centering in 3 Columns
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create 3 columns, with equal width
        col1, col2, col3 = st.columns([1, 2, 1])  # The middle column (col2) will be wider
        
        # Place the hero image in the center column (col2)
        with col2:
            if os.path.exists(hero_image_path):
                st.image(hero_image_path, use_column_width=True, caption="Take Control of Your Health")
            else:
                st.error("Hero image not found.")
    
    
        # # Features Overview Section
        # st.subheader("Overview of the Features")
        # st.markdown("<br>", unsafe_allow_html=True)
    
        # col1, col2, col3, col4 = st.columns(4)
    
        # # Define a uniform height for the expanders
        # expander_height_style = "min-height: 140px; padding: 10px; text-align: center;"
    
        # with col1:
        #     img = load_and_resize_image(feature_images["info"], size=(80, 80))
        #     if img:
        #         st.image(img, caption="PCOS Information", width=100)
        #     with st.expander("PCOS Information"):
        #         st.markdown(f"<div style='{expander_height_style}'>Learn about the symptoms, causes, and management strategies.</div>", unsafe_allow_html=True)
    
        # with col2:
        #     img = load_and_resize_image(feature_images["assessment"], size=(80, 80))
        #     if img:
        #         st.image(img, caption="Simple Risk Assessment", width=100)
        #     with st.expander("Simple Risk Assessment"):
        #         st.markdown(f"<div style='{expander_height_style}'>Quickly assess your risk based on key symptoms.</div>", unsafe_allow_html=True)
    
        # with col3:
        #     img = load_and_resize_image(feature_images["enhanced"], size=(80, 80))
        #     if img:
        #         st.image(img, caption="Enhanced Risk Assessment", width=100)
        #     with st.expander("Enhanced Risk Assessment"):
        #         st.markdown(f"<div style='{expander_height_style}'>Provide more detailed health data for an in-depth risk evaluation.</div>", unsafe_allow_html=True)
    
        # with col4:
        #     img = load_and_resize_image(feature_images["results"], size=(80, 80))
        #     if img:
        #         st.image(img, caption="Results Visualization", width=100)
        #     with st.expander("Results Visualization"):
        #         st.markdown(f"<div style='{expander_height_style}'>View your risk prediction and result with visualizations.</div>", unsafe_allow_html=True)
        
        # Features Overview Section
        st.subheader("Overview of the Features")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create 4 equal-width columns for the feature cards
        col1, col2, col3, col4 = st.columns(4)
        
        # Define a consistent card style
        card_style = """
            <div style="
                background-color: #f8f4ff;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 3px 3px 12px rgba(0, 0, 0, 0.1);
                transition: transform 0.3s ease-in-out;
                min-height: 350px; /* Ensures all cards have the same height */
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            " onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
                {image}
                <h4 style="color: #6d3bb3; margin-top: 10px;">{title}</h4>
                <p style="font-size: 14px; color: #555; margin-top: 5px;">{description}</p>
            </div>
        """
                
        # Generate each feature card
        with col1:
            img = load_and_resize_image(feature_images["info"], size=(80, 80))
            image_html = f'<img src="data:image/png;base64,{get_base64(feature_images["info"])}" width="80">' if img else ""
            st.markdown(card_style.format(image=image_html, title="PCOS Information", description="Understand what PCOS is, its symptoms, causes, and impact on women's health. Learn about common treatment options and lifestyle changes to manage symptoms effectively."), unsafe_allow_html=True)
        
        with col2:
            img = load_and_resize_image(feature_images["assessment"], size=(80, 80))
            image_html = f'<img src="data:image/png;base64,{get_base64(feature_images["assessment"])}" width="80">' if img else ""
            st.markdown(card_style.format(image=image_html, title="Simple Risk Assessment", description="Take a quick questionnaire based on key PCOS symptoms like irregular periods and weight changes. Get an instant indication of potential risk."), unsafe_allow_html=True)
        
        with col3:
            img = load_and_resize_image(feature_images["enhanced"], size=(80, 80))
            image_html = f'<img src="data:image/png;base64,{get_base64(feature_images["enhanced"])}" width="80">' if img else ""
            st.markdown(card_style.format(image=image_html, title="Enhanced Risk Assessment", description="For a more accurate evaluation, enter detailed health data including hormonal levels, ultrasound results, and medical history. This provides better insights into potential risk."), unsafe_allow_html=True)
        
        with col4:
            img = load_and_resize_image(feature_images["results"], size=(80, 80))
            image_html = f'<img src="data:image/png;base64,{get_base64(feature_images["results"])}" width="80">' if img else ""
            st.markdown(card_style.format(image=image_html, title="Results Visualization", description="Receive a clear and easy-to-understand visualization of your assessment results. Graphs and insights will help you interpret your risk level and guide your next steps toward better health."), unsafe_allow_html=True)


    
        # Call to Action
        st.markdown("<h3 style='text-align: center; margin-top: 40px;'>Start your journey towards better health...</h3>", unsafe_allow_html=True)
    
        # Add space between markdown and button
        st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical space 

        # Disclaimer Section
        st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are based on available data from a specific patient dataset. <a href="https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos" target="_blank">Access the dataset here</a></li>
                <li>The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor for diagnosis and treatment.</li>
                <li>The accuracy of predictions is limited by the dataset's scope and quality, and results may not apply to everyone.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    except Exception as e:
        st.error("No internet connection detected. Please check your network and try again.")
        st.stop()  # Stop execution in case of an error.


# Run the home page function when the script is executed
if __name__ == "__main__":
    home_page()