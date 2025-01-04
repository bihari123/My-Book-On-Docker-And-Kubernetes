import time
from datetime import datetime
import os

LOG_FILE = "./data/app.log"

# Create data directory if it doesn't exist
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def write_log():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{timestamp} - Application is running\n"
        
        with open(LOG_FILE, "a") as f:
            f.write(message)
            print(f"Wrote to log: {message}", end="")
        
        time.sleep(5)

if __name__ == "__main__":
    print("Starting application...")
    print(f"Logs will be written to: {LOG_FILE}")
    write_log()
