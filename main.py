from fastapi import FastAPI
import wikipedia
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your specific allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# @app.get("/")
# async def get_wikipedia_url(topic: str):
#     try:
#         # Search for the page title using wikipedia library
#         page = wikipedia.page(topic)
#         url = page.url
#     except Exception:
#         url = "https://en.wikipedia.org/wiki/Main_Page"
#     return {"topic": topic, "url": url}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
