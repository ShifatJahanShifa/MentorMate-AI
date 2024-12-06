from fastapi.middleware.cors import CORSMiddleware

def configure_cors(app):
    origins = [
        "http://localhost:3000",  # Example: Frontend running on localhost:3000
        "https://your-frontend-domain.com",  # Example: Add your frontend's domain
        "*",  # Allow all domains (use cautiously in production)
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # Allows all origins or specific ones
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allows all headers
    )
