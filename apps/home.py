# apps/home_app.py
import streamlit as st

def home_page():
    st.markdown(
    """
    <div style='text-align: left;'>
        <h1>Medical Analysis Assistant</h1>
    </div>
    """,
    unsafe_allow_html=True,
    )
    
    st.markdown("")
    
    # What is Medical Analysis section
    st.markdown(
        "Medical analysis involves the systematic examination of health data, symptoms, and diagnostic information to assess potential health conditions. "
        "This application uses machine learning algorithms to provide preliminary assessments for various medical conditions. "
        "These tools can help identify potential health risks and guide users toward appropriate medical consultation. "
        "Early detection and analysis can significantly improve health outcomes and treatment effectiveness."
    )
    
    st.markdown("")
    
    # Main Features section
    st.markdown("**Main Features**")
    st.markdown(
        "The features available in this application range from cardiovascular assessment to infectious disease detection. "
        "Each tool is designed to analyze specific health indicators and provide meaningful insights based on established medical research."
    )
    st.caption("access options from sidebar menu ←")
    
    st.markdown("")
    
    # Feature list with descriptions
    st.markdown("**1. Heart Disease Prediction** – Analyzes cardiovascular risk factors to assess the likelihood of heart disease based on clinical parameters.")
    
    st.markdown("**2. Tuberculosis Detection** – Uses chest X-ray analysis to identify potential signs of tuberculosis infection in lung tissues.")
    
    st.markdown("**3. Skin Cancer Classification** – Evaluates dermatological images to detect potential malignant skin lesions and classify cancer types.")
    
    st.markdown("**4. Health Assistant Chat** – Provides interactive consultation for general health questions and medical guidance.")

    st.markdown("")
    st.markdown("")
    st.divider()
    
    st.caption(
        "<span style='font-size: small;'>Note: This application is designed for educational and screening purposes only.</span>\n\n"
        "<span style='font-size: small;'>Always consult with qualified healthcare professionals for accurate diagnosis and treatment decisions.</span>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    home_page()