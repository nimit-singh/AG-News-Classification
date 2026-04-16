import streamlit as st

st.set_page_config(page_title="News Classifier", page_icon="📰", layout="centered")

st.title("🧠 AI-Powered News Classification System")

st.markdown(
    """
Classify news articles into **World, Sports, Business, or Sci/Tech** using Natural Language Processing (NLP) and Machine Learning.
"""
)

st.markdown("---")

st.subheader("🎯 Project Overview")

st.write(
    """
This application classifies news articles into predefined categories using **Machine Learning**.

👉 Categories:
- 🌍 World  
- 🏏 Sports  
- 💼 Business  
- 💻 Sci/Tech  
"""
)
with st.expander("📊 Dataset Details"):
    st.write(
        """
- Source: AG News Dataset  
- Type: Multiclass Text Classification  
- Fields: Title + Description  
- Classes: 4 Categories  
"""
    )

with st.expander("📂 Data Format"):
    st.write(
        """
| Title | Description | Category |
|------|-------------|----------|
| Market rises | Stocks hit new high | Business |
| Team wins match | Final score announced | Sports |
"""
    )

with st.expander("⚙️ How It Works"):
    st.write(
        """
1️⃣ Input news text (Title/Description)  
2️⃣ Text preprocessing  
3️⃣ TF-IDF vectorization  
4️⃣ Model prediction  
5️⃣ Output category  
"""
    )

st.markdown("---")
st.subheader("⚡ Features")

st.write(
    """
✔ Manual News Classification  
✔ Bulk CSV Prediction  
✔ Model Performance Insights  
✔ Fast ML Model  
✔ Interactive UI using Streamlit  
"""
)

st.markdown("---")

st.subheader("🧪 Example")

st.markdown("**Input:** Apple launches new AI-powered iPhone")
st.markdown("**Output:** 💻 Sci/Tech")

st.markdown("---")


st.info("🚀 Start by choosing a feature below")

col1, col2 = st.columns(2)

with col1:
    if st.button("✍️ Manual Prediction"):
        st.switch_page("pages/1_✍️_Manual_Prediction.py")

with col2:
    if st.button("📂 Bulk Prediction"):
        st.switch_page("pages/2_📂_Bulk_Prediction.py")
