from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

                                    
def get_gemini_response(input,pdf_content,prompt):
    """
    This function is used to get the response from the gemini api
    """
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input ,pdf_content[0], prompt])

    return response.text


def input_pdf_setup(uploaded_file):
    """
    This function is used to get the pdf content from the uploaded file
    """
    if uploaded_file is not None:

        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = images[0]

        # convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # to encode to base64
            }
        ]

        return pdf_parts
    
    else:
        raise FileNotFoundError("No file uploaded")
    


# Streamlit application (UI)
    

st.set_page_config(page_title = "ATS Resume Expert")
st.header("ATS Tracking System Version: 0.0.1")

input_text = st.text_area("Job Description: ",key = "input") #JD

uploaded_file = st.file_uploader("Upload your Resume (in pdf format): ", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Sucessfully")


submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("What are the Keywords That are Missing")

submit4 = st.button("Percentage Match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""     

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text,pdf_content,input_prompt1)

        st.subheader("The Response is :")
        st.write(response)
    
    else:
        st.write("Please Upload the resume")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text,pdf_content,input_prompt3)

        st.subheader("The Response is :")
        st.write(response)
    
    else:
        st.write("Please Upload the resume")