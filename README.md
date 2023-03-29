# chatbot

Simple front-end web app to query a chatbot server. Simply swap out `app.query()` with whatever API you're using to query the chatbot.

## Quickstart

Just install requirements
```
pip install -r requirements.txt
```

Secret information (e.g. API keys) are in `secrets.py`. Once these are configured, then spin up a Flask server with 
```
make deploy
```

Then point your browser to
```
localhost:8765
```
