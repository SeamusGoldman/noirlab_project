"""
Celestial object routes are defined in this module. The routes allow creating, reading, updating, and deleting
celestial objects in the database. The routes are implemented using FastAPI's APIRouter, and the route functions use
the SQLModel Session dependency to interact with the database.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud.celestial_crud import (
    create_celestial,
    delete_celestial,
    get_all_celestials,
    get_celestial,
    update_celestial,
)
from app.database import get_session
from app.schemas.celestial_schema import CelestialCreate, CelestialRead, CelestialUpdate

celestial_router = APIRouter(prefix="/celestial", tags=["Celestial Objects"])


# Create a celestial object
@celestial_router.post("/", response_model=CelestialRead, status_code=201)
def create_celestial_object(celestial: CelestialCreate, db: Session = Depends(get_session)):
    return create_celestial(db, celestial)


# Get all celestial objects
@celestial_router.get("/", response_model=list[CelestialRead])
def read_all_celestial_objects(db: Session = Depends(get_session)):
    return get_all_celestials(db)


# Get a celestial object by ID
@celestial_router.get("/{celestial_id}", response_model=CelestialRead)
def read_celestial_object(celestial_id: int, db: Session = Depends(get_session)):
    celestial = get_celestial(db, celestial_id)
    if celestial is None:
        raise HTTPException(status_code=404, detail="Celestial object not found")
    return celestial


# Update a celestial object
@celestial_router.put("/{celestial_id}", response_model=CelestialRead)
def update_celestial_object(celestial_id: int, celestial_update: CelestialUpdate, db: Session = Depends(get_session)):
    updated_celestial = update_celestial(db, celestial_id, celestial_update)
    if updated_celestial is None:
        raise HTTPException(status_code=404, detail="Celestial object not found")
    return updated_celestial


# Delete a celestial object
@celestial_router.delete("/{celestial_id}", status_code=204)
def delete_celestial_object(celestial_id: int, db: Session = Depends(get_session)):
    result = delete_celestial(db, celestial_id)
    if not result:
        raise HTTPException(status_code=404, detail="Celestial object not found")
