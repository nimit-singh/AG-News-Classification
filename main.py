import streamlit as st
import joblib

# Load model
model = joblib.load("News_Classificatiom_Model_LR.joblib")

# Page config
st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align: center;'>📰 News Classification App</h1>",
    unsafe_allow_html=True,
)
# st.switch_page(
#     "C:\\Users\\singh\\OneDrive\\Desktop\\NLP\\Project\\AG News Classification Dataset Done\\pages\\Bulk_scanner.py"
# )
st.markdown("---")

# Input section
st.subheader("Enter News Article")
Input = st.text_area("Type or paste your news here...", height=200)

st.markdown("---")

# Button
if st.button("🔍 Classify"):
    if Input.strip() == "":
        st.warning("⚠️ Please enter a news article.")
    else:
        prediction = model.predict([Input])[0]

        categories = {1: "🌍 World", 2: "🏏 Sports", 3: "💼 Business", 4: "💻 Sci/Tech"}

        predicted_category = categories.get(prediction, "Unknown")

        st.success(f"✅ Predicted Category: {predicted_category}")
