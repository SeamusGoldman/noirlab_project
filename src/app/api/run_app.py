"""
This module is the entry point for the FastAPI application. It creates an instance of FastAPI and includes the API
routes defined in the celestial_routes module. The main function starts the FastAPI application using Uvicorn.
"""

from fastapi import FastAPI

from app.api.celestial_routes import celestial_router

app = FastAPI(title="Astronomy API")

# Include API routes
app.include_router(celestial_router)


def main():
    import uvicorn

    uvicorn.run("app.api.run_app:app", host="0.0.0.0", port=8000, reload=True)
