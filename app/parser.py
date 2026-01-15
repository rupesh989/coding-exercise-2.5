import os
from datetime import datetime

LOG_DIR = "logs"

def parse_logs():
    logs = []
    log_id = 1

    for file in os.listdir(LOG_DIR):
        if file.endswith(".log"):
            with open(os.path.join(LOG_DIR, file), "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        ts, level, comp, msg = line.strip().split("\t")
                        logs.append({
                            "id": log_id,
                            "timestamp": datetime.strptime(ts, "%Y-%m-%d %H:%M:%S"),
                            "level": level.upper(),
                            "component": comp,
                            "message": msg
                        })
                        log_id += 1
                    except:
                        # Skip malformed lines
                        continue
    return logs
    
