import streamlit as st
import joblib
import pandas as pd
import json
from io import StringIO, BytesIO

model = joblib.load("News_Classificatiom_Model_LR.joblib")

st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

st.title("🔎 Bulk Premium Scanner")
col1, col2, col3 = st.columns([3, 3, 3])
# st.markdown(
#     "<h1 style='text-align: center;'>📰 Bulk Premium Scanner</h1>",
#     unsafe_allow_html=True,
# )

sample_data1 = {
    "Title": ["Global Markets Rally Amid Economic Recovery Hopes"],
    "Description": [
        "Stock markets worldwide are experiencing a surge as investors anticipate a strong economic recovery."
    ],
}
sample_data2 = {
    "Title": [
        "Local Team Wins Championship After Thrilling Final",
    ],
    "Description": [
        "In an exhilarating match, the local team clinched the championship title, marking their first victory in a decade.",
    ],
}
sample_data = {
    "Title": ["Tech Giant Unveils Latest Smartphone Model"],
    "Description": [
        "The tech giant has announced its newest smartphone, featuring cutting-edge technology and innovative design.",
    ],
}


# with col1:
#     st.download_button(
#         label="📥 Download Sample CSV", data=csv_data, file_name="sample.csv"
#     )
# with col2:
#     st.download_button(
#         label="📥 Download Sample Excel", data=excel_data, file_name="sample.xlsx"
#     )
# with col3:
#     st.download_button(
#         label="📥 Download Sample json", data=json_data, file_name="sample.json"
#     )

st.title("📂 Upload Your File")
uploaded_file = st.file_uploader(
    "Choose a file", type=["csv", "xlsx", "json"], accept_multiple_files=False
)

if uploaded_file is not None:
    st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")
    st.subheader("📄 File Preview")
    df = pd.DataFrame(uploaded_file)
    st.dataframe(df.head(10))

buffer = BytesIO()

# csv_data = df.to_csv(index=False)
# excel_data = df.to_excel(buffer, index=False)
# excel_data = buffer.getvalue()
# json_data = df.to_json(orient="records")

st.markdown("---")

st.subheader("🔍 Classify Uploaded File")

st.write("Click the button below to classify the uploaded file.")

if st.button("🔍 Classify"):
    if uploaded_file is None:
        st.warning("⚠️ Please upload a file.")
    else:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file, encoding="utf-8")
            elif uploaded_file.name.endswith(".xlsx"):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith(".json"):
                df = pd.read_json(uploaded_file)
            else:
                st.error("Unsupported file format.")
                st.stop()

            if "Description" not in df.columns:
                st.error("The file must contain a 'Description' column.")
                st.stop()

            content = " ".join(df["Description"].astype(str).tolist())

        except Exception as e:
            st.error(f"Error processing file: {e}")
            st.stop()
        prediction = model.predict([content])[0]

        categories = {1: "🌍 World", 2: "🏏 Sports", 3: "💼 Business", 4: "💻 Sci/Tech"}

        predicted_category = categories.get(prediction, "Unknown")

        st.success(f"✅ Predicted Category: {predicted_category}")
