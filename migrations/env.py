from logging.config import fileConfig

from alembic import context
from sqlmodel import SQLModel, create_engine

from app.models.celestial_model import *

# Load Alembic config
config = context.config
fileConfig(config.config_file_name)

# Set metadata for migrations
target_metadata = SQLModel.metadata

# Database connection URL
DATABASE_URL = "postgresql://admin:Noirlabrules!@db:5432/db"  # Ensure this matches your database

engine = create_engine(DATABASE_URL)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
