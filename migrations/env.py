import os

from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel

from app.models import celestial_model  # Import all your models

# Load DATABASE_URL from environment, with a fallback default
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://noirlab_user:admin@localhost:5432/noirlab_db")

# Load Alembic configuration
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)  # ✅ Override alembic.ini setting

# Ensure Alembic knows your database schema
target_metadata = SQLModel.metadata


def run_migrations_online():
    """Run migrations in 'online' mode by connecting to the database."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


def run_migrations_offline():
    """Run migrations in 'offline' mode (for generating migration scripts)."""
    context.configure(url=DATABASE_URL, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
