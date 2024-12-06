from fastapi import FastAPI
from googleapiclient.discovery import build
from typing import List

app = FastAPI()

YOUTUBE_API_KEY = "AIzaSyDCzeW65HECZ2pmPYrQMhyr1Pv9FIQvD0o"

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

