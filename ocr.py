import easyocr
import streamlit as st
from PIL import Image
import numpy as np

st.title("Easy OCR: extract text from image")

image = st.file_uploader(label = "upload your image here", type=['png','jpg','jpeg'])

if image is not None:
  input_image = Image.open(image)
  st.image(input_image)
                         
  with st.spinner("AI is at work!"):
    reader = easyocr.Reader(['en', 'es']) # need to run only once to load model into memory
    result = reader.readtext(np.array(input_image))
    result_text = []
    for text in result:
        result_text.append(text[1])
    st.write(result_text)
    st.success("here you go!")
else:
    st.write("upload an image")

st.header("Language Translator :smile:")

from mtranslate import translate
import pandas as pd
import os
import pyautogui

text = ' '.join(result_text)
if len(text) > 0:
  try:
    output = translate(text,'en')
    st.text_area("Translated Text is ",output,height=200)
  except Exception as e:
    st.error(e)
translate=translator.translate(text,lang_tgt="en")
st.write(translate)
