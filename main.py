
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse 
app = FastAPI()

origins = [
    "http://localhost:5174",  # Frontend running on port 5174
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Only allow requests from the frontend port
    allow_credentials=True,  # Allow credentials (e.g., cookies, auth headers)
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend"}


@app.get("/chatbot")
async def chatbot():
    return RedirectResponse(url="http://localhost:8501") 

@app.get("/pdf")
async def pdf():
    return RedirectResponse(url="http://localhost:8502")


@app.get("/aivoice")
async def pdf():
    # Redirect to the Streamlit app
    return RedirectResponse(url="http://localhost:8503")