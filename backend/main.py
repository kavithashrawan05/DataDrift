from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="DataDrift Deal Intelligence Backend",
    description="Backend API for the AI-powered Deal Intelligence Agent",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "DataDrift Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }