-- 테이블 생성
CREATE TABLE tracks (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  artist TEXT,
  bpm INTEGER,
  genre TEXT
);

-- 데이터 삽입
INSERT INTO tracks VALUES (1,'Midnight Loop','You',128,'Lo-fi');
INSERT INTO tracks VALUES (2,'Solar Drift','You',140,'Ambient');

-- 전체 조회
SELECT * FROM tracks;

-- 조건 조회
SELECT * FROM tracks WHERE bpm > 130;

-- plays 테이블 생성
CREATE TABLE plays (
  track_id INTEGER,
  played_at TEXT
);

-- plays 데이터 삽입
INSERT INTO plays VALUES (1,'2024-01-01');
INSERT INTO plays VALUES (1,'2024-01-02');
INSERT INTO plays VALUES (2,'2024-01-03');

-- JOIN으로 재생 횟수 조회
SELECT t.title, COUNT(p.track_id) AS play_count
FROM tracks t
LEFT JOIN plays p ON t.id = p.track_id
GROUP BY t.title;