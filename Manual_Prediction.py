import streamlit as st
import joblib


# Load model
model = joblib.load("News_Classificatiom_Model_LR.joblib")

# Page config
st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")


# Title
st.title("📰 AG News Classifier")
st.markdown(
    "Classify news articles into **World, Sports, Business, or Sci/Tech** using Machine Learning."
)

st.expander("🧠 About This Tool").write(
    """
This tool classifies news articles into one of four categories:

- 🌍 **World** – International news, politics, global events  
- ⚽ **Sports** – Matches, teams, tournaments  
- 💼 **Business** – Economy, markets, companies  
- 💻 **Sci/Tech** – Technology, AI, science innovations  

👉 Simply enter a news article and click **Predict** to see the result.
"""
)


st.expander("✍️ Input Guidelines").write(
    """
- Enter at least **1–2 sentences** for better accuracy  
- Avoid very short text like single words  
- You can paste full news articles or headlines  
"""
)
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
