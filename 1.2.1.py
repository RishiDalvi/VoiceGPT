import openai # to interact with openai generative
import speech_recognition as sr # speech to text
import streamlit as st   #Streamlit Environment

import pyttsx3# Initialize TTS enginey
engine = pyttsx3.init()# Set TTS rate and volume
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.setProperty('volume', 1)




rec=sr.Recognizer()#For  Recognizing voice input
openai.api_key='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'  #calling gpt API
model='text-davinci-002' # Language model used to get the result from VoiceGPT


def Generative_v(prompt):
    response = openai.Completion.create(engine=model, prompt=prompt, n=1, stop=None, max_tokens=412, temperature=0.7)
    message = response.choices[0].text.strip()
    st.write(message)
    for i in range(1,3):
        if i == 1:
            engine.say(message)
            engine.startLoop(False)
            engine.iterate()
            engine.endLoop()
            break
        else:
            print("RunTimeError")
    
    return

       

def Generative(prompt):
    response = openai.Completion.create(engine=model, prompt=prompt, n=1, stop=None, max_tokens=412, temperature=0.7)
    message = response.choices[0].text.strip()
    return message

    


st.sidebar.header('VoiceGPT')
add_input_format=st.sidebar.selectbox('Choose an option', ('Text to Text','Text to Speech','Speech to Text','Speech to Speech'))

if add_input_format=='Text to Text':
    txt_in = st.text_input('**INPUT:**')
    hit = st.button('**SUBMIT**')
    if hit:
        content = Generative(txt_in)# Calling the Generative function with text input
        st.write(content)


if add_input_format=='Text to Speech':
    txt_in = st.text_input('**INPUT:**')
    hit = st.button('**SUBMIT**')
    if hit:
        content_v = Generative_v(txt_in)# Calling the Generative function with text input
        st.write(content_v)# printing the generated response
        

if add_input_format=='Speech to Text':
    with sr.Microphone() as Input: # accessing the system microphone
            s_n=st.button('speak now')
            if s_n:
                audio = rec.listen(Input)    # getting the audio input 
                try:
                    text = rec.recognize_google(audio) # converting the voice into text
                    st.write(text)
                    content=Generative(text) #Calling the Generative function
                    st.write(content)# printing the generated response 
                except sr.UnknownValueError:
                    print('I cannot understand you')
                except sr.RequestError:
                    print('I could not get the request')          
            
if add_input_format=='Speech to Speech':
    with sr.Microphone() as Input: # accessing the system microphone
            s_n=st.button('speak now')
            if s_n:
                audio = rec.listen(Input)    # getting the audio input 
                try:
                    text = rec.recognize_google(audio) # converting the voice into text
                    st.write(text)
                    content_v=Generative_v(text) #Calling the Generative function
                    st.write(content_v)# printing the generated response 
                except sr.UnknownValueError:
                    print('I cannot understand you')
                except sr.RequestError:
                    print('I could not get the request')
                             

                


