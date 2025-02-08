from fastapi import FastAPI

from app.api import celestial_routes

# # Ensure `src/` is in Python's import path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))


app = FastAPI()

app.include_router(celestial_routes.router)

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
