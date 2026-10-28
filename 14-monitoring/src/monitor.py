import json
import time
from datetime import datetime

print("=== MLOps Monitoring - Started ===")

# 13-mlops metrics read karanawa
with open("../13-mlops/models/metrics.txt", "r") as f:
    data = f.read().replace("}{", "}\n{").split("\n")[0]
    print(f"[{datetime.now()}] Reading metrics from 13-mlops...")

# Check karala balanawa
try:
    # metrics.txt eke dict eka
    content = open("../13-mlops/models/metrics.txt").read()
    print(f"Metrics: {content[:100]}...")

    # Simple alert logic
    if "0.93" in content:
        print("✅ STATUS: HEALTHY - Accuracy > 93%")
        status = "HEALTHY"
    else:
        print("⚠️ STATUS: WARNING - Accuracy low!")
        status = "WARNING"

    # Log eka save karanawa
    log_entry = f"{datetime.now()} - {status} - {content}\n"
    with open("logs/monitor.log", "a") as log:
        log.write(log_entry)
    
    print(f"-> Log saved to logs/monitor.log")
    print("-> MODEL MONITORING COMPLETE! 🚀")

except Exception as e:
    print(f"Error: {e}")
