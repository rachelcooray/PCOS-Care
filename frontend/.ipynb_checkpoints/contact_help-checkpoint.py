import streamlit as st
import os

# Update paths to be relative to the current file location
current_directory = os.path.dirname(__file__)
logo_path = os.path.join(current_directory, "images/logo.png")

def contact_help_page():
    # Layout for logo and title
    col1, col2 = st.columns([1, 4])

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    # Contact & Help Section with better formatting and structure
    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
    st.subheader("Help & Contact")
    
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Need Assistance?</h3>
        <p>If you have any questions or encounter issues while using the app, feel free to reach out to us:</p>
        <p><strong>Email:</strong> <a href='mailto:w1956444@my.westminster.ac.uk'>w1956444@my.westminster.ac.uk</a></p>
        <p><strong>Phone:</strong> +44 12 345 6789</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Feedback Section with a background color
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Feedback & Suggestions</h3>
        <p>We value your feedback! Please share your experience or suggestions with us via email at:</p>
        <p><strong>Email:</strong> <a href='mailto:w1956444@my.westminster.ac.uk'>w1956444@my.westminster.ac.uk</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Privacy and Data Handling Section
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
        <h3 style='text-align: center; color: #b179d9;'>Privacy & Data Handling</h3>
        <p>We respect your privacy. All data provided will not be stored for future use or shared with third parties.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # FAQ Section with Expanders
    st.subheader("Frequently Asked Questions (FAQs)")

    with st.expander("How do I use the PCOS Risk Assessment Tool?"):
        st.markdown("""
        Simply fill in your details in the input fields on the home page and click submit. The results will be displayed on the next page.
        """)

    with st.expander("Can I get a detailed report of my risk assessment?"):
        st.markdown("""
        Yes, you can get a detailed report of your risk assessment, which includes a summary and prediction. You can also download it as a PDF for your reference.
        """)

    with st.expander("What happens if I don't fill out all the fields?"):
        st.markdown("""
        All fields are required for an accurate risk assessment. Please ensure you fill in all the details to proceed with the analysis.
        """)

    with st.expander("Is my data safe?"):
        st.markdown("""
        Yes, privacy is taken seriously. Your data is not stored beyond the prediction session and is only used for assessment purposes.
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
        The accuracy is limited by the quality and scope of the training data, which consists of 541 patient records from Kerala, India.
        """)

    with st.expander("Does this tool integrate with healthcare systems?"):
        st.markdown("""
        No, this is a standalone web-based tool and currently does not integrate with any electronic medical records or healthcare systems.
        """)

    # Disclaimer Section
    st.markdown("""
        <div style='background-color: #EAE0F5; padding: 20px; border-radius: 10px; border: 2px solid #CDC1FF;'>
            <h3 style='text-align: center; color: #b179d9;'>Disclaimer</h3>
            <ul style='list-style-type: disc; padding-left: 20px;'>
                <li>The prediction given on this platform is based on a dataset of <strong>541 patients from Kerala, India</strong>.</li>
                <li><strong>This is not a medical diagnosis.</strong> It is similar to a preliminary assessment and should not be used as a substitute for clinical evaluation.</li>
                <li>The accuracy of predictions is <strong>limited by the dataset's scope and quality</strong>, and results may not generalize to all populations.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
