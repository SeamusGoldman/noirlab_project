"""
This module contains the Celestial model.

The Celestial model is a SQLModel class that represents a celestial object.
"""

from sqlmodel import Field, SQLModel


class Celestial(SQLModel, table=True):
    """
    Celestial model.

    Attributes:
    - id: int (primary key defaut is turned off of that the id is auto-generated)
    - name: str (indexed field to allow for searching)
    - type: str
    - distance_ly: float (distance in light years)
    - description: str
    """

    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: str
    distance_ly: float
    description: str = Field(default="No description")
