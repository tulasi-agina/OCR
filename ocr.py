import easyocr as ocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("Easy OCR: extract text from image")

image = st.file_uploader(label = "upload your image here, type=['png','jpg','jpeg'])

if image is not None:
  input_image = Image.open(image)
  st.image(input_image)
                         
  with st.spinner("AI is at work!")
    result = reader.readtext(np.array(input_image))
    result_text = []
    for text in result:
        result_text.append(text[1])
    st.write(result_text)
    st.success("here you go!")
else:
    st.write("upload an image")
