import streamlit as st
import joblib
import pandas as pd
import json
from io import BytesIO

st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

model = joblib.load("News_Classification_Model_LR.joblib")

st.title("🔎 Bulk News Classification")
st.markdown("---")

st.markdown("### 📥 Sample Files")

st.write(
    "Download a sample file to understand the required format for bulk classification."
)

st.info(
    """
👉 Required Columns:
- Title  
- Description  
"""
)

sample_df = pd.DataFrame(
    {
        "Title": ["Stock market rises"],
        "Description": ["Investors show positive sentiment"],
    }
)

st.caption("🧪 Example format")
st.dataframe(sample_df)

st.caption("📁 Supported formats: CSV, Excel (.xlsx), JSON")

col1, col2, col3 = st.columns(3)
sample = pd.DataFrame(
    {
        "Title": [
            "Global markets rally amid economic recovery",
            "India wins cricket world cup final",
            "Apple unveils new AI-powered iPhone",
            "Government announces new tax reforms",
            "Scientists discover new exoplanet",
            "Football team secures championship victory",
            "Stock prices fall due to inflation concerns",
            "Tech company launches advanced AI model",
        ],
        "Description": [
            "Stock markets worldwide surge as investors expect strong economic growth.",
            "The team secured a historic win in the finals with outstanding performance.",
            "The latest iPhone features advanced AI capabilities and improved performance.",
            "New policies aim to boost economic growth and stabilize the market.",
            "Astronomers have found a potentially habitable planet outside our solar system.",
            "The underdog team defeated champions in a thrilling final match.",
            "Investors react negatively as inflation rates continue to rise.",
            "The company introduced a cutting-edge AI model for automation and analytics.",
        ],
    }
)
with col1:
    st.download_button("📄 CSV", sample.to_csv(index=False), "sample.csv")

with col2:
    buffer = BytesIO()
    sample.to_excel(buffer, index=False)
    st.download_button(
        "📊 Excel",
        buffer.getvalue(),
        "sample.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

with col3:
    st.download_button(
        "🧾 JSON",
        sample.to_json(orient="records", indent=4),
        "sample.json",
        mime="application/json",
    )

st.markdown("---")

st.markdown("### 📂 Upload Your File")

st.write("Upload your dataset to classify multiple news articles instantly.")

uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "json"])

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        data = json.load(uploaded_file)
        df = pd.DataFrame(data)
    else:
        st.error("❌ Unsupported file format")
        st.stop()

    st.subheader("📊 Preview")
    st.dataframe(df.head())

    if "Title" not in df.columns or "Description" not in df.columns:
        st.error("❌ File must contain 'Title' and 'Description' columns")
        st.stop()

    if st.button("🚀 Classify Data"):

        with st.spinner("🔍 Classifying news articles..."):

            combined_text = df["Title"] + " " + df["Description"]

            predictions = model.predict(combined_text.tolist())
            probs = model.predict_proba(combined_text.tolist())

            categories = {
                1: "🌍 World",
                2: "🏏 Sports",
                3: "💼 Business",
                4: "💻 Sci/Tech",
            }

            df["Prediction"] = predictions
            df["Prediction"] = df["Prediction"].map(categories)
            df["Confidence (%)"] = probs.max(axis=1) * 100

        st.success("✅ Classification Completed!")

        st.subheader("📈 Results")
        st.dataframe(df)

        st.subheader("📊 Prediction Summary")

        col1, col2, col3, col4 = st.columns(4)
        counts = df["Prediction"].value_counts()

        col1.metric("🌍 World", counts.get("🌍 World", 0))
        col2.metric("🏏 Sports", counts.get("🏏 Sports", 0))
        col3.metric("💼 Business", counts.get("💼 Business", 0))
        col4.metric("💻 Tech", counts.get("💻 Sci/Tech", 0))

        st.subheader("📊 Distribution")
        st.bar_chart(df["Prediction"].value_counts())

        csv_output = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "📥 Download Results",
            data=csv_output,
            file_name="classified_results.csv",
            mime="text/csv",
        )
st.markdown("---")
if st.button("🔗 Back to Home"):
    st.switch_page("1_🏠_Home.py")
