import streamlit as st
import csv
import json
import os
import io

def csv2json(file):
    # Read CSV content
    file.seek(0)
    csv_content = file.read().decode('utf-8').splitlines()
    csv_reader = csv.reader(csv_content)

    # Check if the CSV has a header row
    header = next(csv_reader, None)
    if header is None or any(not field for field in header):
        st.error("The uploaded CSV file does not have a valid header row.")
        return None

    # Use DictReader to read CSV with headers
    csv_dict_reader = csv.DictReader(csv_content)
    data = [row for row in csv_dict_reader]

    # Convert to JSON
    json_output = json.dumps(data, indent=2, ensure_ascii=False)
    return json_output

# Streamlit app
st.title("CSV to JSON Converter")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    # Convert CSV to JSON
    json_data = csv2json(uploaded_file)

    if json_data:
        # Display JSON output
        st.text_area("JSON Output", json_data, height=300)

        # Download JSON file
        json_file_path = os.path.splitext(uploaded_file.name)[0] + '.json'
        st.download_button(label="Download JSON file", data=json_data, file_name=json_file_path, mime="application/json")
