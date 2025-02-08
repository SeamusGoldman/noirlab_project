from fastapi import FastAPI

from app.api import celestial_routes

app = FastAPI()
app.include_router(celestial_routes.router)


def main():
    import uvicorn

    uvicorn.run("app.api.run_app:app", host="0.0.0.0", port=8000, reload=True)
