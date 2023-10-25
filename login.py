import streamlit as st
import json
import pandas as pd

st.title("JSON File Viewer")

# Create a login page
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Define a flag to track whether the user is authenticated
authenticated = False

if st.button("Login"):
    # Replace these values with your actual username and password
    if username == "kalyan" and password == "123":
        st.success("Login successful!")
        authenticated = True  # Set the authentication flag to True

# If the user is authenticated, show the upload and display page
if authenticated:
    st.header("Upload JSON File")
    json_file = st.file_uploader("Upload a JSON file", type=["json"])

    if json_file:
        st.subheader("JSON Content")
        try:
            data = json.load(json_file)

            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                df = pd.DataFrame(data)
                st.write(df)
            else:
                st.error("The JSON file should contain a list of dictionaries to be displayed in a table.")
        except json.JSONDecodeError:
            st.error("Invalid JSON file. Please upload a valid JSON file.")