import streamlit as st
import joblib
import pandas as pd
import json
from io import StringIO, BytesIO

# from Manual_Prediction import model

model = joblib.load("News_Classificatiom_Model_LR.joblib")
bytes = BytesIO()
st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

st.title("🔎 Bulk Premium Scanner")
col1, col2, col3 = st.columns([3, 3, 3])
st.markdown(
    "Upload a CSV file with a **text column** to classify multiple news articles."
)

sample_csv = pd.DataFrame(
    {
        "Title": [
            "Global Markets Rally Amid Economic Recovery",
            "Football Team Wins Championship Final",
            "New Smartphone Launches with AI Features",
            "Government Announces New Policy Reforms",
        ],
        "Description": [
            "Stock markets worldwide surge as investors expect strong recovery.",
            "The underdog team secured a historic victory in the finals.",
            "Tech company introduces advanced AI-powered smartphone.",
            "New reforms aim to improve economic growth and stability.",
        ],
    }
)
sample_excel = pd.DataFrame(
    {
        "Title": [
            "Global Markets Rally Amid Economic Recovery",
            "Football Team Wins Championship Final",
            "New Smartphone Launches with AI Features",
            "Government Announces New Policy Reforms",
        ],
        "Description": [
            "Stock markets worldwide surge as investors expect strong recovery.",
            "The underdog team secured a historic victory in the finals.",
            "Tech company introduces advanced AI-powered smartphone.",
            "New reforms aim to improve economic growth and stability.",
        ],
    }
)
sample_json = pd.DataFrame(
    {
        "Title": [
            "Global Markets Rally Amid Economic Recovery",
            "Football Team Wins Championship Final",
            "New Smartphone Launches with AI Features",
            "Government Announces New Policy Reforms",
        ],
        "Description": [
            "Stock markets worldwide surge as investors expect strong recovery.",
            "The underdog team secured a historic victory in the finals.",
            "Tech company introduces advanced AI-powered smartphone.",
            "New reforms aim to improve economic growth and stability.",
        ],
    }
)

csv_data = sample_csv.to_csv(index=False)
with col1:
    st.download_button(
        label="📥 Download Sample CSV", data=csv_data, file_name="sample.csv"
    )
sample_excel = sample_excel.to_excel(bytes, index=False)
with col2:
    st.download_button(
        label="Download Sample Excel",
        data=bytes.getvalue(),
        file_name="sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
json_data = sample_json.to_json(orient="records", indent=4)
with col3:
    st.download_button(
        label="Download Sample JSON",
        data=json_data,
        file_name="sample.json",
        mime="application/json",
    )

st.markdown("---")


uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])
if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, encoding="utf-8")
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".json"):
        data = json.load(uploaded_file)
        df = pd.DataFrame(data)
        st.write("Preview of Uploaded Data:")
        st.dataframe(df.head())
    else:
        st.error("Unsupported file type. Please upload a CSV, Excel, or JSON file.")
        st.stop()
    if "Title" not in df.columns or "Description" not in df.columns:
        st.error("File must contain 'Title' and 'Description' columns.")
        st.stop()
    if st.button("🔍 Classify Bulk Data"):
        Combined = df["Title"] + " " + df["Description"]
        prediction = model.predict(Combined.tolist())
        categories = {1: "🌍 World", 2: "🏏 Sports", 3: "💼 Business", 4: "💻 Sci/Tech"}
        df["Prediction"] = prediction
        df["Prediction"] = df["Prediction"].map(categories)
        st.dataframe(df)
        csv_output = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Classified Results",
            data=csv_output,
            file_name="classified_results.csv",
            mime="text/csv",
        )
