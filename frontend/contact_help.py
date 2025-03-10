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
    st.subheader("Contact & Help")
    
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>
        <h3 style='text-align: center;'>Need Assistance?</h3>
        <p>If you have any questions or encounter issues while using the app, feel free to reach out to us:</p>
        <p><strong>Email:</strong> <a href='mailto:example@email.com'>example@email.com</a></p>
        <p><strong>Phone:</strong> +0123456789</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Feedback Section with a background color
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>
        <h3 style='text-align: center;'>Feedback & Suggestions</h3>
        <p>We value your feedback! Please share your experience or suggestions with us via email at:</p>
        <p><strong>Email:</strong> <a href='mailto:example@email.com'>example@email.com</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Privacy and Data Handling Section
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 20px; border-radius: 10px;'>
        <h3 style='text-align: center;'>Privacy & Data Handling</h3>
        <p>We respect your privacy. All data provided will not be stored for future use or shared with third parties.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # FAQ Section with Expanders
    st.subheader("Frequently Asked Questions (FAQ)")

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

    st.markdown("TO ADD - disclaimer, references")
