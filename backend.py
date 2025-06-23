from fastapi import FastAPI, HTTPException, Response
import os
from dotenv import load_dotenv

load_dotenv()

# Print environment variables after loading .env
# print("After loading .env:")
# print("API_TOKEN:", os.getenv("API_TOKEN"))
# print("WEB_UNLOCKER_ZONE:", os.getenv("WEB_UNLOCKER_ZONE"))

from models import NewsRequest
from utils import generate_broadcast_news, text_to_audio_elevenlabs_sdk
from news_scraper import NewsScraper
from reddit_scraper import scrape_reddit_topics

app = FastAPI()

@app.post("/generate-news-audio")
async def generate_news_audio(request: NewsRequest):
    try:
        results = {}
        
        if request.source_type in ["news", "both"]:
            news_scraper = NewsScraper()
            results["news"] = await news_scraper.scrape_news(request.topics)
        
        if request.source_type in ["reddit", "both"]:
            results["reddit"] = await scrape_reddit_topics(request.topics)

        news_data = results.get("news", {})
        reddit_data = results.get("reddit", {})
        news_summary = generate_broadcast_news(
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            news_data=news_data,
            reddit_data=reddit_data,
            topics=request.topics
        )

        audio_path = text_to_audio_elevenlabs_sdk(
            text=news_summary,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
            output_dir="audio"
        )

        if audio_path and os.path.exists(audio_path):
            with open(audio_path, "rb") as f:
                audio_bytes = f.read()

            return Response(
                content=audio_bytes,
                media_type="audio/mpeg",
                headers={"Content-Disposition": "attachment; filename=news-summary.mp3"}
            )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=1234, reload=True)
