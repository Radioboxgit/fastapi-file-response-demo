# FastAPI Audio Book Generator( Text To Speech)
we are building an audio book generator i.e. an API that Converts text input to audio (speech synthesis) with an option to save the audio locally .
With that we want to show how to return files(image,audio,video) in **FastAPI** 



The Project exposes three routes:

Home Route that redirects to the docs: (http://127.0.0.1:8000/docs)

Voices Route, this returns all the locally available voices(gender): (http://127.0.0.1:8000/voices)

Transcribe Route that returns audio of an given text passed to the route : http://127.0.0.1:8000/synthesize

# Quick Start Guide:
# Step One:
clone this repo:
```
git clone https://github.com/Radioboxgit/fastapi-file-response-demo

```

# Step Two:
cd in to the cloned directory:

```
cd fastapi-file-response-demo

```
# Step Three:
hit the server up and running:

```
uvicorn main:app --reload

```
# Step Four:
clone the react demo for the project

```
git clone https://github.com/Radioboxgit/react-fastapi-file-response-demo

```
# Step Five:
cd into react-fastapi-file-response-demo, install the dependencies needed
and get the server running
```
cd react-fastapi-file-response-demo
npm install
npm run start
```

Voila!!!!, you now have a full fledged audio book generator at your disposal.


