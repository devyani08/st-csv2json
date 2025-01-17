import streamlit as st
import csv
import json
import os

def csv2json(file):
    # Convert CSV file to JSON
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

    # Create JSON output
    json_output = json.dumps(data, indent=2, ensure_ascii=False)
    return json_output

# Streamlit app
st.title("CSV to JSON Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Convert CSV to JSON
    json_data = csv2json(uploaded_file)

    # Display JSON output
    st.text_area("JSON Output", json_data, height=300)

    # Download JSON file
    json_file_path = os.path.splitext(uploaded_file.name)[0] + '.json'
    st.download_button(label="Download JSON file", data=json_data, file_name=json_file_path, mime="application/json")
