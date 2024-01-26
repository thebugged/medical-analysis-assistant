import streamlit as st
from openai import OpenAI

def chat_page():
    st.subheader("Health Assistant", divider='grey')
    st.markdown("")
    st.caption("Go ahead, ask me anything!")

    api_key = st.text_input("Enter your OpenAI GPT-3 API key:")

    if api_key:
        client = OpenAI(api_key=api_key)
        user_input = st.text_input("Ask a health-related question:")

        if st.button("Get Answer"):
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=user_input,
                stream=False,
            )

            st.text("Chatbot's Response:")
            st.text(response['choices'][0]['text'])
    # else:
    #     st.warning("Please enter your OpenAI GPT-3 API key.")

if __name__ == "__main__":
    chat_page()
