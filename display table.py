import streamlit as st
import json
import pandas as pd

st.title("JSON File Viewer")

# Upload JSON file
json_file = st.file_uploader("Upload a JSON file", type=["json"])

if json_file:
    st.subheader("JSON Content")

    try:
        # Read and parse the JSON content
        data = json.load(json_file)

        # Check if the data is a list of dictionaries (common JSON structure)
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            # If it's a list of dictionaries, convert it to a Pandas DataFrame and display it as a table
            df = pd.DataFrame(data)
            st.write(df)
        else:
            st.error("The JSON file should contain a list of dictionaries to be displayed in a table.")

    except json.JSONDecodeError:
        st.error("Invalid JSON file. Please upload a valid JSON file.")