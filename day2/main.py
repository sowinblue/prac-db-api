from fastapi import FastAPI

app = FastAPI()

# 메모리 DB
tracks = [
    {"id": 1, "title": "Midnight Loop", "bpm": 128}
]


# 전체 트랙 조회
@app.get("/tracks")
def get_tracks():
    return tracks

# 트랙 추가
@app.post("/tracks")
def create_track(track: dict):
    tracks.append(track)
    return track

# 특정 트랙 조회
@app.get("/tracks/{id}")
def get_track(id: int):
    for track in tracks:
        if track["id"] == id:
            return track
    return {"error": "Not found"}

# 트랙 수정
@app.put("/tracks/{id}")
def update_track(id: int, updated: dict):
    for track in tracks:
        if track["id"] == id:
            track.update(updated)
            return track
    return {"error": "Not found"}

# 트랙 삭제
@app.delete("/tracks/{id}")
def delete_track(id: int):
    global tracks
    tracks = [t for t in tracks if t["id"] != id]
    return {"message": "deleted"}