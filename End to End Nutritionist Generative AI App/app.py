import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
from google import genai

# Load env


# Create client
client = genai.Client(api_key="")

def get_gemini_response(prompt, image):
    response = client.models.generate_content(
        model="gemini-pro-vision",
        contents=[prompt, image]
    )
    return response.text


# ---------- UI ----------
st.set_page_config(page_title="Calories Advisor App")
st.header("🥗 Gemini Health App")

uploaded_file = st.file_uploader(
    "Upload food image",
    type=["jpg", "jpeg", "png"]
)

image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

if st.button("Tell me about total calories"):
    if image is None:
        st.warning("Please upload an image")
    else:
        prompt = """
        You are a nutrition expert.
        Analyze the food image and estimate:
        1. Calories
        2. Nutrients
        3. Health impact
        """
        result = get_gemini_response(prompt, image)
        st.subheader("🍽️ Nutrition Analysis")
        st.write(result)
