from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LogRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "DevOps Mentor AI is running 🚀"}


@app.post("/analyze-log")
def analyze_log(request: LogRequest):

    log = request.text.lower()

    if "docker" in log:
        return {
            "problem": "Docker permission issue",
            "root_cause": "User is not in docker group",
            "fix": "Run: sudo usermod -aG docker $USER"
        }

    elif "permission denied" in log:
        return {
            "problem": "Permission denied error",
            "root_cause": "Insufficient file/system permissions",
            "fix": "Check user permissions or use sudo"
        }

    else:
        return {
            "problem": "Unknown error",
            "root_cause": "Cannot classify log",
            "fix": "Check logs manually or extend rules"
        }
