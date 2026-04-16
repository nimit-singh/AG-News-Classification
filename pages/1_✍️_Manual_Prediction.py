import streamlit as st
import joblib


st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

model = joblib.load("News_Classification_Model_LR.joblib")

st.title("✍️ Manual News Classification")
st.markdown(
    """
Classify news articles into **World, Sports, Business, or Sci/Tech** using Machine Learning.
"""
)

with st.expander("🧠 About This Tool"):
    st.write(
        """
This tool classifies news articles into one of four categories:

- 🌍 **World** – International news, politics, global events  
- ⚽ **Sports** – Matches, teams, tournaments  
- 💼 **Business** – Economy, markets, companies  
- 💻 **Sci/Tech** – Technology, AI, science innovations  

👉 Enter a news article and click **Classify** to see the result.
"""
    )

with st.expander("✍️ Input Guidelines"):
    st.write(
        """
- Enter at least **1–2 sentences** for better accuracy  
- Avoid very short text like single words  
- You can paste full news articles or headlines  
"""
    )

st.markdown("---")

st.subheader("Enter News Article")
import random

samples = [
    "Apple launches new AI-powered smartphone with advanced features",
    "India wins cricket world cup final in a thrilling match",
    "Stock markets fall due to global economic uncertainty",
    "New breakthrough in quantum computing announced by scientists",
]


if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ✅ Sample button
if st.button("🧪 Try Sample"):
    st.session_state.input_text = random.choice(samples)

Input = st.text_area("Type or paste your news here...", height=200, key="input_text")

st.markdown("---")

if st.button("🔍 Classify"):

    if Input.strip() == "":
        st.warning("⚠️ Please enter a news article.")
    else:
        with st.spinner("🔍 Analyzing news..."):

            prediction = model.predict([Input])[0]
            probs = model.predict_proba([Input])

        categories = {
            1: "🌍 World",
            2: "🏏 Sports",
            3: "💼 Business",
            4: "💻 Sci/Tech",
        }

        predicted_category = categories.get(prediction, "Unknown")
        confidence = max(probs[0]) * 100

        st.markdown("### 📊 Prediction Result")

        st.success(f"Category: {predicted_category}")
        st.progress(int(confidence))
        st.caption(f"Confidence: {confidence:.2f}%")

st.markdown("---")

if st.button("📂 Go to Bulk Prediction"):
    st.switch_page("pages/2_📂_Bulk_Prediction.py")
