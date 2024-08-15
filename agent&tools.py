#agent&tools.py
import streamlit as st  # type: ignore
from complex_agent import ComplexAgent

def main():
    st.title("Advanced Multi-Tool Chatbot")

    # Create ComplexAgent instance
    agent = ComplexAgent()
    user_input = st.text_input("Enter your command:")

    if st.button("Submit"):
        if user_input:
            try:
                response = agent.process_input(user_input)
                st.write(response)
            except Exception as e:
                st.write(f"An error occurred: {str(e)}")
        else:
            st.write("Please enter some input.")

if __name__ == "__main__":
    main()
