from fastapi import FastAPI

app = FastAPI()

# 메모리 DB
tracks = [
    {"id": 1, "title": "Midnight Loop", "bpm": 128}
]
