from fastapi import FastAPI
import wikipedia

app = FastAPI()

@app.get("/")
async def get_wikipedia_url(topic: str):
    try:
        # Search for the page title using wikipedia library
        page = wikipedia.page(topic)
        url = page.url
    except Exception:
        url = "https://en.wikipedia.org/wiki/Main_Page"
    return {"topic": topic, "url": url}

