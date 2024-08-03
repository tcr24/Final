from fastapi import FastAPI, Request
import logging
from app.dependencies import get_settings
from app.routers import users
from fastapi.responses import JSONResponse

app = FastAPI()

# Include your routers
app.include_router(users.router)

logger = logging.getLogger("uvicorn.error")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    try:
        response = await call_next(request)
    except Exception as exc:
        logger.error(f"Error processing request: {exc}")
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
    return response

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup complete.")
