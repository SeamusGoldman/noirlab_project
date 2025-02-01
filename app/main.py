import os
import sys

from fastapi import FastAPI

# Ensure Python finds `app/` as a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.api import celestial_routes

app = FastAPI()

app.include_router(celestial_routes.router)


def main():
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
