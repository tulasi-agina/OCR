import streamlit as st
from mtranslate import translate
import speech_recognition as sr

r = sr.Recognizer()

st.header("Convert Audio to Text")
uploadedAudioFile = st.file_uploader(label = "upload your audio file here", type=['mp3','wav'])

if uploadedAudioFile is not None:
    audio_bytes = uploadedAudioFile.read()
    st.audio(audio_bytes,format='audio/wav') #this will let user play the user-uploaded audio file
    
    with open(uploadedAudioFile.name,"wb") as f:
        f.write(uploadedAudioFile.getbuffer())
    
    sound = uploadedAudioFile.name
    f = open("sourcefile.txt","w+")
    with sr.AudioFile(sound) as source:
        audio_data = r.record(source)
        f.write(r.recognize_google(audio_data, language='es-ES'))
        f.close()
	
else:
  pass
