# Day 2 — REST API


## 엔드포인트 목록
| Method | Path | 설명 |
|--------|------|------|
| GET | /tracks | 전체 목록 조회 |
| POST | /tracks | 트랙 추가 |
| GET | /tracks/{id} | 특정 트랙 조회 |
| PUT | /tracks/{id} | 트랙 수정 |
| DELETE | /tracks/{id} | 트랙 삭제 |

## 오늘 배운 개념
- REST API = HTTP 메서드로 URL을 통해 데이터를 구별하는 규약
- FastAPI = REST API를 쉽고 빠르게 만들 수 있는 Python 프레임워크
- Swagger UI = FastAPI 내장 API 문서화/테스트 도구
- 미들웨어 = 요청이 실제 처리되기 전에 실행되는 함수
- CORS = 다른 주소에서 오는 요청을 허용할지 말지 설정하는 보안 정책
- JWT = 로그인 상태를 증명하는 토큰