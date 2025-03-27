import streamlit as st
import google.generativeai as genai

def chat_page():
    st.subheader("Health Assistant", divider='grey')
    st.caption("Access your API key from your [Google AI Studio](https://makersuite.google.com/app/apikey)")
    st.markdown("")
    st.caption("Go ahead, ask me anything!")

    api_key = st.text_input("Enter your Google AI (Gemini) API key:", placeholder="AIza...")

    if api_key:
        genai.configure(api_key=api_key)
        
        user_input = st.text_input("Ask a health-related question:")

        if st.button("Get Answer"):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                system_instruction = "You are a helpful health assistant."
                
                prompt = f"{system_instruction}\n\nUser question: {user_input}"
                response = model.generate_content(prompt)
                
                st.subheader("Chatbot's Response:")
                st.markdown(response.text) 
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.error("Please ensure you're using a valid Google AI API key.")

if __name__ == "__main__":
    chat_page()
