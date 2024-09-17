import uvicorn
from fastapi import FastAPI
from app.api.v1.routes import router  # Import your API router

app = FastAPI()

# Include your API routes
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
