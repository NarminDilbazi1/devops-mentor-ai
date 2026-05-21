from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()   # 👈 BU MÜTLƏQ ƏVVƏL OLMAQLIDIR

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            "root_cause": "Insufficient permissions",
            "fix": "Use sudo or check file permissions"
        }

    return {
        "problem": "Unknown error",
        "root_cause": "Cannot classify log",
        "fix": "Extend rules"
    }
