import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.api.run_app import app
from app.database import get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_celsetial(client: TestClient):
    response = client.post(
        "/celestial/",
        json={
            "name": "Test Star",
            "type": "Star",
            "distance_ly": 4.2,
            "description": "A test star in the Alpha Centauri system.",
        },
    )
    data = response.json()

    assert response.status_code == 201
    assert data["name"] == "Test Star"
    assert data["type"] == "Star"
    assert data["distance_ly"] == 4.2


def test_get_all_celestial_objects(client: TestClient):
    """Test retrieving all celestial objects."""
    # First, create an object
    client.post(
        "/celestial/",
        json={
            "name": "Test Planet",
            "type": "Planet",
            "distance_ly": 10.5,
            "description": "A test planet in a distant galaxy.",
        },
    )

    response = client.get("/celestial/")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_celestial_by_id(client: TestClient):
    """Test retrieving a celestial object by its ID."""
    # First, create an object
    create_response = client.post(
        "/celestial/",
        json={
            "name": "Test Nebula",
            "type": "Nebula",
            "distance_ly": 500,
            "description": "A beautiful test nebula.",
        },
    )
    created_data = create_response.json()
    object_id = created_data["id"]

    # Fetch by ID
    response = client.get(f"/celestial/{object_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == object_id
    assert data["name"] == "Test Nebula"


def test_update_celestial(client: TestClient):
    """Test updating an existing celestial object."""
    # First, create an object
    create_response = client.post(
        "/celestial/",
        json={
            "name": "Test Comet",
            "type": "Comet",
            "distance_ly": 3.2,
            "description": "A passing comet.",
        },
    )
    created_data = create_response.json()
    object_id = created_data["id"]

    # Update the object
    response = client.put(
        f"/celestial/{object_id}",
        json={
            "name": "Updated Comet",
            "type": "Comet",
            "distance_ly": 3.2,
            "description": "A newly discovered comet.",
        },
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Updated Comet"
    assert data["description"] == "A newly discovered comet."


def test_delete_celestial(client: TestClient):
    """Test deleting a celestial object."""
    # First, create an object
    create_response = client.post(
        "/celestial/",
        json={
            "name": "Test Black Hole",
            "type": "Black Hole",
            "distance_ly": 1000.0,
            "description": "A simulated black hole.",
        },
    )
    created_data = create_response.json()
    object_id = created_data["id"]

    # Delete the object
    delete_response = client.delete(f"/celestial/{object_id}")
    assert delete_response.status_code == 204

    # Try fetching it again (should return 404)
    get_response = client.get(f"/celestial/{object_id}")
    assert get_response.status_code == 404
