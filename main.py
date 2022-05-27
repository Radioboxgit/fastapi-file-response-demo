import pyttsx3  
from fastapi import FastAPI
from fastapi.responses import FileResponse,RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from gtts import gTTS

app=FastAPI()

engine = pyttsx3.init()  
voice_gender={'female':1,'male':0}
voices = engine.getProperty('voices')   


app=FastAPI(description ="TEXT TO SPEECH(READ ALOUD) APP ",
title="TTS",
version="0.0.1")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def docs():
    # redirect to docs 
    return RedirectResponse(url='/docs')

@app.get('/voices')
def get_voices():
    voices =engine.getProperty('voices')
    return [ (voice.name,voice.id) for voice in voices] 


@app.get('/synthesize')
async def tts(text:str, voice:str='male', rate:int='180'):
    engine.setProperty('rate', rate)
    voice_id=voice_gender[voice]
    engine.setProperty('voice', voices[voice_id].id)
    engine.save_to_file(text, "voice.mp3")
    engine.runAndWait()
    return FileResponse('voice.mp3',media_type="audio/mp3")




