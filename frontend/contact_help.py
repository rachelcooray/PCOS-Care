import streamlit as st
import os

logo_path = "./images/logo.png"

def contact_help_page():
    col1, col2 = st.columns([1, 4])  

    with col1:
        if os.path.exists(logo_path):
            st.image(logo_path, width=100)  
        else:
            st.error("Logo image not found.")

    with col2:
        st.title("PCOS Care")

    st.subheader("Contact & Help")
    st.markdown("""
    ### Need Assistance?  
    If you have any questions or encounter issues while using the app, feel free to reach out to us at:  
    **Email**: [example@email.com]  
    **Phone**: +0123456789   

    ### Feedback & Suggestions  
    We value your feedback! Please share your experience or suggestions on **Email**: [example@email.com] with us to improve the app. 

    ### Privacy & Data Handling  
    We respect your privacy. All data provided will not be stored for future use or shared with third parties.
    """)
    
    st.markdown("<hr style='border: 1px solid #ccc; margin-top: 50px;'>", unsafe_allow_html=True)
    
    # FAQ Section with Expanders
    st.subheader("Frequently Asked Questions (FAQ)")

    with st.expander("How do I use the PCOS Risk Assessment Tool?"):
        st.markdown("""
        Simply fill in your details in the input fields on the home page and click submit. The results will be displayed on the next page.
        """)

    with st.expander("Can I get a detailed report of my risk assessment?"):
        st.markdown("""
        The tool provides a summary of your risk with a prediction and visualization.
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
        No, this is a standalone web-based tool and does not integrate with electronic medical records or healthcare systems.
        """)
