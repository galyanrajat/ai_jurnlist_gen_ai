NewsNinja - Stealthy News Aggregator

Your personal news ninja that silently gathers headlines and Reddit reactions, then delivers audio briefings straight to your ears. *No scroll, just soul.*

---
FEATURES
- 🗞️ Scrape premium news websites (bypassing paywalls)
- 🕵️♂️ Extract live Reddit reactions (even from JS-heavy threads)
- 🔊 AI-powered audio summaries (text-to-speech with ElevenLabs)
- ⚡ Real-time updates (thanks to Bright Data's MCP magic)

---
PREREQUISITES
- Python 3.9+
- Bright Data account (https://brightdata.com)
- ElevenLabs account (https://elevenlabs.io)

---
QUICK START

1. Clone the Dojo

https://github.com/galyanrajat/ai_jurnlist_gen_ai.git
```


2. Install Dependencies
```
pip install -r requirements.txt
```

3. Ninja Secrets (Environment Setup)
Create .env file:
```
.enc
```

Configure your secrets in .env:
```
# Bright Data
BRIGHTDATA_MCP_KEY="your_mcp_api_key"
BROWSER_AUTH="your_browser_auth_token"

# ElevenLabs 
ELEVENLABS_API_KEY="your_text_to_speech_key"
```

4. Prepare Your Weapons (Bright Data Setup)
- Create MCP zone: https://brightdata.com/cp/zones
- Enable browser authentication
- Copy credentials to .env

---
RUNNING THE NINJA

First terminal (Backend):
```
 python backend.py
```

Second terminal (Frontend):
```
 streamlit run frontend.py
```

---
PROJECT STRUCTURE
```
.
├── frontend.py          # Streamlit UI
├── backend.py           # API & data processing  
├── utils.py             # UTILS  
├── news_scraper.py      # News Scraper  
├── reddit_scraper.py    # Reddit Scraper  
├── models.py            # Pydantic model
├── Pipfile              # Dependency scroll
├── .env.example         # Secret map template
└── requirements.txt     # Alternative dependency list
```

---
NOTES
- First scrape takes 15-20 seconds 
- Reddit scraping uses real browser emulation via MCP
- Keep .env file secret (jurnilist never reveal their tools)

---
SUPPORT
Bright Data support: https://brightdata.com/support

*"In the darkness of information overload, be the ninja."* 🌑"# ai_jurnlist_gen_ai" 

![backend_running](F:\vscode main\ai_jurnilistmain\code_run (1).png)
![Streamlit_running](F:\vscode main\ai_jurnilistmain\streamlit run.png)