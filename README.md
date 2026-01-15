# Log File REST API

FastAPI based REST API to read, filter and analyze log files.

## Features
- Read logs from directory
- Filter by level, component and time
- Statistics API
- Get log by ID
- Pagination support

## Run locally
```bash
1. python -m venv venv

2. venv\Scripts\activate

3. pip freeze > requirements.txt

4. pip install -r requirements.txt

5. pip install fastapi uvicorn pydantic

6. uvicorn app.main:app --reload
