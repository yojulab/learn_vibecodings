# Docker Context for Gemini

This file explains the Docker setup for the "learn_vibecodings" project.

## Files

- `docker-compose.yml`: Defines the services, networks, and volumes for the application stack. It likely orchestrates the different containers that make up the application.
- `Dockerfile`: Defines the custom environment and dependencies for one of the application's services. This is the blueprint for building a Docker image.
- `.env`: Contains environment variables specific to the Docker Compose setup, such as service configurations, ports, or credentials.

## How to Use

To run the application using Docker, you would typically use the following command from within this directory:

```bash
docker-compose up
```

To run it in detached mode (in the background):

```bash
docker-compose up -d
```

To stop the services:

```bash
docker-compose down
```
