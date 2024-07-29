from dotenv import load_dotenv
import streamlit as st
import os
from openai import import OpenAI

load_dotenv()
MODEL = 'gpt-4o'
client = OpenAI(api_key=os.getenv('openai key = sk-proj-7ZutYe4BtEydXRvY2NO2T3BlbkFJugnHv5sHcraW6Np8Vyk8'))

st.title('AI AUDIO ANALYZER')
audio_format = ['mp3', 'wav', 'm4a']
audio_file = st.file_uploader('upload an audio file', type=audio_format)


if audio_file:
    st.audio(audio_file)

    transcription = client.audio.transcriptions.create(
        model = 'whisper-1',
        file = audio_file
    )

    response = client.chat.completions.create(
            model = MODEL,
            messages=[
                {"role": "system", "content": """You are an audio analyzer AI. Analyze the audio and create a summary of the provided transcription. Response in Markdown."""},
                {"role": "user", "content": f"The audio transcript is: {transcription.text}"}
            ],
            temperature=0,
        )
    st.markdown(response.choices[0.message.content])
