# FastAPI Audio Book Generator( Text To Speech)
Project showing how to return files in FastAPI

This demo project is all about how to return files e.g. image, audio, video etc in FASTAPI.

The Project exposes three routes:

Home Route that redirects to the docs: (http://127.0.0.1:8000/docs)

Voices Route, this returns all the locally available voices(gender): (http://127.0.0.1:8000/voices)

Transcribe Route that returns audio of an given text passed to the route : http://127.0.0.1:8000/synthesize

# Quick Start Guide:
# step one:
clone this repo:
```
git clone https://github.com/Radioboxgit/fastapi-file-response-demo

```

# step two:
cd in to the cloned directory:

```
cd fastapi-file-response-demo

```
# step three:
hit the server up and running:

```
uvicorn main:app --reload

```
# step four:
clone the react demo for the project

```
git clone https://github.com/Radioboxgit/react-fastapi-file-response-demo

```
# step five:
cd into react-fastapi-file-response-demo, install the dependencies needed
and get the server running
```
cd react-fastapi-file-response-demo
npm install
npm run start
```

Voila!!!!, you now have a full fledged audio book generator at you disposal.


