from pydantic import BaseModel


class CelestialBase(BaseModel):
    """
    Celestial base schema.It contains the common attributes for the Celestial schemas.

    Attributes: ()
    - name: str
    - type: str
    - distance_ly: float
    """

    name: str
    type: str
    distance_ly: float


class CelestialCreate(CelestialBase):
    """
    Celestial create schema.

    Attributes:
    - description: str
    """

    description: str = "No description"


class CelestialUpdate(CelestialBase):
    """
    Celestial update schema.

    Attributes: (all are optional since this is an update schema)
    - name: str
    - type: str
    - distance_ly: float
    - description: str
    """

    name: str = None
    type: str = None
    distance_ly: float = None
    description: str = None


class CelestialRead(CelestialBase):
    """
    Celestial read schema.

    Attributes:
    - id: int
    - description: str (default is "No description")
    """

    id: int
    description: str

    class Config:
        from_attributes = True  # This tells Pydantic to create a Pydantic model from the attributes of the ORM model.
