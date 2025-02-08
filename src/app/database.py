"""
This file is responsible for creating the database connection and session.
"""

import os

from sqlmodel import Session, create_engine

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:Noirlabrules!@db:5432/db")

engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    """
    Get a new session from the database.
    """
    with Session(engine) as session:
        yield session
