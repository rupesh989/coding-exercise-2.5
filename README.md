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
pip install -r requirements.txt
uvicorn app.main:app --reload
