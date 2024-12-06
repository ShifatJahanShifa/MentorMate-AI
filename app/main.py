from fastapi import FastAPI, File, UploadFile
from googleapiclient.discovery import build
from typing import List
import os
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI, Depends
from schema import Base, Subject, Topic, Subtopic, ReadingResource  # Import models
from fastapi import HTTPException
import shutil


DATABASE_URL = "sqlite:///./test.db"  # SQLite database file

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a sessionmaker object for DB interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create FastAPI app
app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create the tables in the database
Base.metadata.create_all(bind=engine)

YOUTUBE_API_KEY = "AIzaSyDCzeW65HECZ2pmPYrQMhyr1Pv9FIQvD0o"

# Path to store uploaded files
UPLOAD_DIRECTORY = "uploaded_books"

@app.get("/")
async def hello():
    return "Hello World!"

# Initialize the YouTube API client
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to fetch videos based on a search query
def search_youtube(query: str, max_results: int = 5) -> List[dict]:
    request = youtube.search().list(
        q=query,
        part='snippet',
        maxResults=max_results,
        type='video'
    )
    response = request.execute()
    
    videos = []
    for item in response['items']:
        video = {
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'video_url': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'thumbnail': item['snippet']['thumbnails']['high']['url']
        }
        videos.append(video)
    
    return videos

# Define an endpoint to search YouTube videos
@app.get("/search_youtube/{query}")
async def search_videos(query: str, max_results: int = 5):
    videos = search_youtube(query, max_results)
    return {"videos": videos}

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

# File upload function
def upload_file(file: UploadFile = File(...)):
    # Define the path where the file will be saved
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)

    # Save the file
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Return the file name (just the name of the file to be saved in the database)
    return file.filename

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    else:
        return {"error": "File not found"}

@app.post("/subjects/")
async def create_subject(name: str, image: UploadFile = File(...), db: SessionLocal = Depends(get_db)):
    # Upload the image file and get the file name
    try:
        image_filename = upload_file(image)  # Upload the image and get the file name
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading image: {str(e)}")

    # Create the subject with the uploaded image filename (or full path if needed)
    db_subject = Subject(name=name, image=image_filename)  # Store just the file name in the database
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)

    return {"id": db_subject.id, "name": db_subject.name, "image": db_subject.image}


    # Delete the file from the server
def delete_file(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        raise HTTPException(status_code=404, detail="File not found")

# Endpoint to delete a subject
@app.delete("/subjects/{subject_id}")
async def delete_subject(subject_id: int, db: SessionLocal = Depends(get_db)):
    # Get the subject from the database
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Delete the associated file
    try:
        delete_file(db_subject.image)  # Delete the file from the server
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error deleting file: {str(e)}")
    
    # Delete the subject from the database
    db.delete(db_subject)
    db.commit()

    return {"message": "Subject deleted successfully"}

# Endpoint to update a subject
@app.put("/subjects/{subject_id}")
async def update_subject(
    subject_id: int, 
    name: str = None, 
    image: UploadFile = File(None),  # Image is optional
    db: SessionLocal = Depends(get_db)
):
    # Get the subject from the database
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()

    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Update the name if provided
    if name:
        db_subject.name = name

    # If a new image is uploaded, replace the old one
    if image:
        try:
            # Delete the old image from the server
            delete_file(db_subject.image)
            # Upload the new image and get the file name
            new_image_filename = upload_file(image)
            db_subject.image = new_image_filename  # Update the image name
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error uploading image: {str(e)}")
    else:
        # If no new image is provided, retain the existing image
        db_subject.image = db_subject.image  # Just to show no change happens

    # Commit the changes to the database
    db.commit()
    db.refresh(db_subject)

    return {"id": db_subject.id, "name": db_subject.name, "image": db_subject.image}

@app.post("/topics/")
async def create_topic(name: str, subject_id: int, db: SessionLocal = Depends(get_db)):
    # Check if the subject exists
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if not db_subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    # Create a new topic
    db_topic = Topic(name=name, subject_id=subject_id)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)

    return {"id": db_topic.id, "name": db_topic.name, "subject_id": db_topic.subject_id}

# Endpoint to update a topic
@app.put("/topics/{topic_id}")
async def update_topic(topic_id: int, name: str = None, subject_id: int = None, db: SessionLocal = Depends(get_db)):
    # Get the topic from the database
    db_topic = db.query(Topic).filter(Topic.id == topic_id).first()

    if not db_topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    # Update the topic's name if provided
    if name:
        db_topic.name = name

    # Update the topic's subject if provided
    if subject_id:
        # Check if the new subject exists
        db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
        if not db_subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        db_topic.subject_id = subject_id

    # Commit the changes to the database
    db.commit()
    db.refresh(db_topic)

    return {"id": db_topic.id, "name": db_topic.name, "subject_id": db_topic.subject_id}

# Endpoint to delete a topic
@app.delete("/topics/{topic_id}")
async def delete_topic(topic_id: int, db: SessionLocal = Depends(get_db)):
    # Get the topic from the database
    db_topic = db.query(Topic).filter(Topic.id == topic_id).first()

    if not db_topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    # Delete the topic from the database
    db.delete(db_topic)
    db.commit()

    return {"message": f"Topic with id {topic_id} deleted successfully"}

    # Endpoint to create a new Subtopic
@app.post("/subtopics/")
async def create_subtopic(name: str, topic_id: int, db: SessionLocal = Depends(get_db)):
    # Check if the topic exists
    db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if not db_topic:
        raise HTTPException(status_code=404, detail="Topic not found")

    # Create new Subtopic and add to DB
    db_subtopic = Subtopic(name=name, topic_id=topic_id)
    db.add(db_subtopic)
    db.commit()
    db.refresh(db_subtopic)

    return {"id": db_subtopic.id, "name": db_subtopic.name, "topic_id": db_subtopic.topic_id}

# Endpoint to update a Subtopic
@app.put("/subtopics/{subtopic_id}")
async def update_subtopic(subtopic_id: int, name: str = None, topic_id: int = None, db: SessionLocal = Depends(get_db)):
    # Get the subtopic from the database
    db_subtopic = db.query(Subtopic).filter(Subtopic.id == subtopic_id).first()
    if not db_subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")

    # Update name and topic_id if provided
    if name:
        db_subtopic.name = name
    if topic_id:
        # Check if the new topic exists
        db_topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if not db_topic:
            raise HTTPException(status_code=404, detail="Topic not found")
        db_subtopic.topic_id = topic_id

    # Commit the changes to the database
    db.commit()
    db.refresh(db_subtopic)

    return {"id": db_subtopic.id, "name": db_subtopic.name, "topic_id": db_subtopic.topic_id}

# Endpoint to delete a Subtopic
@app.delete("/subtopics/{subtopic_id}")
async def delete_subtopic(subtopic_id: int, db: SessionLocal = Depends(get_db)):
    # Get the subtopic from the database
    db_subtopic = db.query(Subtopic).filter(Subtopic.id == subtopic_id).first()
    if not db_subtopic:
        raise HTTPException(status_code=404, detail="Subtopic not found")

    # Delete the subtopic
    db.delete(db_subtopic)
    db.commit()

    return {"message": f"Subtopic {subtopic_id} deleted successfully"}