
# MentorMate

"Mentor Mate", a web application for facilitating the teachers to be trained for delivering the better education to their students using the power of API and AI.


## Introduction

"Mentor Mate" is a web based application, developed by our team DU_Twilight. We used the cutting edge technology, power of AI and API to build this application. The application is meant to facilitate teachers to get prepared before they go to their classrooms. The goal of our application is to help our teachers get training facilities. Teachers can explore their interested resources in several ways 


## Features

- User friendly web application
- Homepage with Subject Selection 
- Learning Options - Step-by-Step Learning,Jump to Topic
- Topic and Resource Variety 
- Teacher Performance Tracking 
- chatbot, powered by Gemini AI
- PDF analyzer, powered by Gemini AI



## Tech Stack

**Frontend:** html, css, javascript, reactjs, tailwindcss

**Backend:** fastAPI, streamlit

**API:** gemini, langchain, youtube, azure cognitive speach service


## Run Locally


### Clone the project

```bash
  git clone https://github.com/ShifatJahanShifa/MentorMate-AI.git
```

### for frontend:

```bash
   cd afia-frontend
   npm install
   npm run dev
```
### for backend

### Activate virtual environment

```bash
   python -m venv "virtual environment name"
  .virtual environment name\Scripts\activate
```

### Install dependencies

```bash 
   pip install -r requirements.txt
```

### Run the project

```bash
   cd app
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

goto folder langchain-PDF-Gemini, create virtual env, install  dependencies as stated before.
to run the streamlit app: 
```
    streamlit run app.py
```
goto folder chatbot, create virtual env, install  dependencies as stated before. to run the streamlit app: 
```
    streamlit run test.py
```
goto folder ai-voice, create virtual env, install  dependencies as stated before. to run the streamlit app: 
``` 
    streamlit run voice_assistant.py
``` 





## Authors

- [@ShifatJahanShifa](https://www.github.com/ShifatJahanShifa)
- [@AfiaLubaina](https://www.github.com/afia-lubaina)
- [@EhsanUddoula](https://www.github.com/EhsanUddoula)

