"""
Celestial CRUD operations. The CRUD operations are implemented using SQLModel's Session dependency to interact with the
database. The operations include creating, reading, updating, and deleting celestial objects.
"""

from sqlmodel import Session, select

from app.models.celestial_model import Celestial
from app.schemas.celestial_schema import CelestialCreate, CelestialUpdate


def create_celestial(db: Session, celestial: CelestialCreate) -> Celestial:
    """
    Create a new celestial object.

    Args:
    - db: Session
    - celestial: CelestialCreate

    Returns:
    - Celestial
    """
    db_celestial = Celestial(**celestial.model_dump())
    db.add(db_celestial)
    db.commit()
    db.refresh(db_celestial)
    return db_celestial


def get_celestial(db: Session, celestial_id: int) -> Celestial | None:
    """
    Get a celestial object by its id.

    Args:
    - db: Session
    - celestial_id: int

    Returns:
    - Celestial | None (if the celestial object is not found)
    """
    return db.exec(select(Celestial).where(Celestial.id == celestial_id)).first()


def get_all_celestials(db: Session) -> list[Celestial]:
    """
    Get all celestial objects.

    Args:
    - db: Session

    Returns:
    - list[Celestial]
    """
    return db.exec(select(Celestial)).all()


def update_celestial(db: Session, celestial_id: int, celestial: CelestialUpdate) -> Celestial | None:
    """
    Update a celestial object.

    Args:
    - db: Session
    - celestial_id: int
    - celestial: CelestialUpdate

    Returns:
    - Celestial | None (if the celestial object is not found)
    """
    db_celestail = get_celestial(db, celestial_id)
    if not db_celestail:
        return None

    update_data = celestial.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_celestail, key, value)

    db.commit()
    db.refresh(db_celestail)
    return db_celestail


def delete_celestial(db: Session, celestial_id: int) -> bool:
    """
    Delete a celestial object.

    Args:
    - db: Session
    - celestial_id: int

    Returns:
    - bool (True if the celestial object was deleted, False otherwise)
    """
    db_celestial = get_celestial(db, celestial_id)
    if not db_celestial:
        return None

    db.delete(db_celestial)
    db.commit()
    return db_celestial
