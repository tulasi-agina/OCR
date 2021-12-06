import easyocr
import streamlit as st
from PIL import Image
import numpy as np
from mtranslate import translate

reader = easyocr.Reader(['en', 'es']) # need to run only once to load model into memory

st.title("Language Translator")

st.header("OCR: extract text from image")

image = st.file_uploader(label = "upload your image here", type=['png','jpg','jpeg'])

if image is not None:
    input_image = Image.open(image)
    st.image(input_image)

if st.button("Translate"):

  if image is not None:

    with st.spinner("AI is at work!"):
      
      result = reader.readtext(np.array(input_image))
      result_text = []
      for text in result:
          result_text.append(text[1])
      #st.write(result_text)
    st.success("here you go!")
  text = ' '.join(result_text)
  st.write(text)
  
  st.header("Language Translator :smile:")

  if len(text) > 0:
    output = translate(text,'en')
    st.text_area("Translated Text is ",output,height=200)
    
    
st.header("Translator: multiple languages")  
text_src = st.text_area("Enter text:", height=200)

# Language ISO Codes used by Python: https://cloud.google.com/translate/docs/languages
src = st.sidebar.selectbox('from', ['en', 'es', 'de', 'fr', 'zh-CN', 'zh-TW'])
tgt = st.sidebar.selectbox('to', ['en', 'es', 'de', 'fr', 'zh-CN', 'zh-TW'])

if st.button('Translate Sentence'):
    if text_src == "":
        st.warning('Please **enter text** for translation')

    else:
        text_tgt = translate(text_src,tgt)
        st.write(text_tgt)
else:
  pass
