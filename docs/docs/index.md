# Installation and Setup

## Clone the Repository

```bash
git clone https://github.com/SeamusGoldman/noirlab_project.git
cd noirlab_project
```

## Run the Application with Docker

If you need docker installed you can run the following commands:

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y docker.io docker-compose

# Ensure Docker starts on boot
sudo systemctl enable --now docker

sudo usermod -aG docker $USER
newgrp docker
```

After Docker is setup and running run the following commands to build the containers.

```bash
docker-compose up -d --build
```

This command will:

- Build and start the application container
- Start a PostgreSQL database container
- Apply any necessary database migrations

## API Documentation

Once running, the API documentation is available at:

This will allow you to interact with the API with out a GUI using SwaggerUI.

- [http://localhost:8000/docs](http://localhost:8000/docs)


## Running Tests

To run tests inside the container:

```bash
docker exec -it <container_name> pytest tests/
```

Replace `<container_name>` with the name of the running application container. You can find it using:

```bash
docker ps
```
