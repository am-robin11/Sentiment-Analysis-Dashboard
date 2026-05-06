from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
from transformers import pipeline
import uvicorn

app = FastAPI()

# Mount static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load the model ONCE at startup
sentiment_pipeline = None

@app.on_event("startup")
async def load_model():
    global sentiment_pipeline
    print("Loading model... please wait.")
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )
    print("Model loaded and ready!")

# Request schemas
class TextInput(BaseModel):
    text: str

class BatchInput(BaseModel):
    texts: List[str]

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/analyze")
async def analyze(input: TextInput):
    result = sentiment_pipeline(input.text[:512])[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4),
        "text": input.text
    }

@app.post("/analyze/batch")
async def analyze_batch(input: BatchInput):
    results = []
    for text in input.texts:
        result = sentiment_pipeline(text[:512])[0]
        results.append({
            "label": result["label"],
            "score": round(result["score"], 4),
            "text": text
        })
    return results

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)