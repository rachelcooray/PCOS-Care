import streamlit as st
import os
import base64

def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

def contact_help_page():
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

    st.subheader("Help & Contact")
    
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Need Assistance?</h3>
        <p>If you have any questions or encounter issues while using the application, feel free to reach out to us:</p>
        <p><strong>Email:</strong> <a href='mailto:w1956444@my.westminster.ac.uk'>w1956444@my.westminster.ac.uk</a></p>
        <p><strong>Phone:</strong> +44 12 345 6789</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Feedback Section with a background color
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Feedback & Suggestions</h3>
        <p>We’d love to hear from you! Share your thoughts or suggestions with us via email at:</p>
        <p><strong>Email:</strong> <a href='mailto:w1956444@my.westminster.ac.uk'>w1956444@my.westminster.ac.uk</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Privacy and Data Handling Section
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Privacy & Data Handling</h3>
        <p>We take your privacy seriously. Any data you provide is only used for this risk assessment and is not stored or shared with third parties.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # FAQ Section with Expanders
    st.subheader("Frequently Asked Questions (FAQs)")

    with st.expander("How do I use the PCOS Risk Assessment Tool?"):
        st.markdown("""
        Simply fill in your details in the input fields on the Risk Assessment page and click submit. The results will be displayed on the Results page.
        """)

    with st.expander("Can I get a detailed report of my risk assessment?"):
        st.markdown("""
        Yes! You can receive a full report with a summary and prediction, and you can download it as a PDF for your reference.
        """)

    with st.expander("What happens if I don't fill out all the fields?"):
        st.markdown("""
        All fields are required for an accurate risk assessment. Make sure you complete everything to get the most accurate results.
        """)

    with st.expander("Is my data safe?"):
        st.markdown("""
        Yes, privacy is taken seriously. Your data is not saved after the session, and it is only used for the assessment.
        """)

    with st.expander("Can I use this tool for someone else?"):
        st.markdown("""
        This tool is designed for personal use, but you can enter details for someone else as long as you have their consent.
        """)

    with st.expander("Is this a medical diagnosis?"):
        st.markdown("""
        No, this tool is intended for preliminary assessment only and should not be used as a substitute for professional medical advice. 
        """)

    with st.expander("What is the accuracy of the prediction?"):
        st.markdown("""
        The accuracy is based on data from 541 patients in Kerala, India, so it may not be 100% accurate for every person.
        """)

    with st.expander("Does this tool integrate with healthcare systems?"):
        st.markdown("""
        No, this is a standalone tool and currently does not link with any medical records or healthcare systems.
        """)

    # Disclaimer Section
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <p style='text-align: center; font-weight: bold;'>This tool is for informational purposes only and does not provide a medical diagnosis.</p>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>Predictions are generated based on data from a specific patient dataset. <a href="https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos" target="_blank">Access the dataset here</a></li>
                <li>The assessment is not a substitute for a professional medical evaluation or diagnosis. Always consult a doctor or qualified healthcare provider for diagnosis and treatment.</li>
                <li>The predictions provided are based on the available dataset and may have limitations in accuracy and scope. Results should be interpreted with caution and may not reflect individual circumstances.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)