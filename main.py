from fastapi import FastAPI, HTTPException
from typing import Optional, List
from datetime import datetime
from .parser import parse_logs
from .models import LogEntry

app = FastAPI(title="Log File REST API")

# Load logs once when server starts
logs = parse_logs()


@app.get("/logs", response_model=List[LogEntry])
def get_logs(
    level: Optional[str] = None,
    component: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None,
    limit: int = 100,
    offset: int = 0
):
    result = logs

    if level:
        result = [l for l in result if l["level"] == level.upper()]

    if component:
        result = [l for l in result if l["component"].lower() == component.lower()]

    if start_time:
        try:
            start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            result = [l for l in result if l["timestamp"] >= start]
        except:
            raise HTTPException(400, "Invalid start_time format")

    if end_time:
        try:
            end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            result = [l for l in result if l["timestamp"] <= end]
        except:
            raise HTTPException(400, "Invalid end_time format")

    return result[offset: offset + limit]


@app.get("/logs/stats")
def get_stats():
    total = len(logs)
    by_level = {}
    by_component = {}

    for l in logs:
        by_level[l["level"]] = by_level.get(l["level"], 0) + 1
        by_component[l["component"]] = by_component.get(l["component"], 0) + 1

    return {
        "total_logs": total,
        "logs_per_level": by_level,
        "logs_per_component": by_component
    }


@app.get("/logs/{log_id}", response_model=LogEntry)
def get_log_by_id(log_id: int):
    for log in logs:
        if log["id"] == log_id:
            return log
    raise HTTPException(status_code=404, detail="Log ID not found")
