import streamlit as st
import joblib

# Load the trained model
model = joblib.load("News_Classificatiom_Model_LR.joblib")

st.title("AG News Classification")
st.write(
    "Enter a news article to classify it into onie of the following categories: World, Sports, Business, Sci/Tech."
)
Input = st.text_area("Enter news article here...", height=200, key="news_input")

if st.button("Classify"):
    if Input.strip() == "":
        st.warning("Please enter a news article to classify.")
    else:
        # Predict the category
        prediction = model.predict([Input])[0]
        categories = {1: "World", 2: "Sports", 3: "Business", 4: "Sci/Tech"}
        predicted_category = categories.get(prediction, "Unknown")
        st.success(f"The predicted category is: {predicted_category}")
