import streamlit as st
from openai import OpenAI

def chat_page():
    st.subheader("Health Assistant", divider='grey')
    st.caption("Access your API key from your [OpenAI account](https://platform.openai.com/api-keys)")
    st.markdown("")
    st.caption("Go ahead, ask me anything!")

    api_key = st.text_input("Enter your OpenAI GPT-3 API key:", placeholder="sk-...e1D2")

    if api_key:
        client = OpenAI(api_key=api_key)
        user_input = st.text_input("Ask a health-related question:")

        if st.button("Get Answer"):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful health assistant."},
                        {"role": "user", "content": user_input}
                    ],
                    max_tokens=150
                )
                st.text("Chatbot's Response:")
                st.text(response.choices[0].message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_page()
