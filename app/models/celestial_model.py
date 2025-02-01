from sqlmodel import Field, SQLModel


class Celestial(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    type: str
    distance: float
    description: str = Field(default="No description")
