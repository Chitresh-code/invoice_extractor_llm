from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
import fitz
from io import BytesIO

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini 1.5 Flash
model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(image):
    prompt = """
    You are an expert in understanding invoices.
    Extract the following details from the uploaded invoice image:
    1. Customer details
    2. Products
    3. Total Amount
    """
    response = model.generate_content([image[0], prompt])
    return response.text

def input_image_details(image):
    if image is not None:
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        bytes_data = buffered.getvalue()
        image_parts = [
            {
                "mime_type": "image/png",
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file found")

def convert_pdf_to_image(uploaded_file):
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        page = pdf_document.load_page(0)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        return img
    else:
        raise FileNotFoundError("No file found")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Invoice Extractor")
st.header("Gemini Invoice Extractor")

uploaded_file = st.file_uploader("Choose an invoice image or PDF...", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "application/pdf":
        image = convert_pdf_to_image(uploaded_file)
    else:
        image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)
    
submit = st.button("Submit")

if submit and uploaded_file is not None:
    if file_type == "application/pdf":
        image_data = input_image_details(image)
    else:
        image_data = input_image_details(image)
        
    response = get_gemini_response(image_data)
    st.subheader("Extracted Details")
    st.write(response)
