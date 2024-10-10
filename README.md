# Services

This is a simple Service-based architecture for a short messages application.
Services are split into User, Messages and Likes based on the business logic they implement.

## Architecture

- The requests from port 80 are processed by API Gateway (Nginx webserver). The API Gateway forwards the requests to the appropriate service based on the path prefix.
- There are 3 services which are written using Python, FastAPI.
- Each service has Swagger interface through which the services can be used.
- The services use MongoDB as the database.
- The services are containerized using Docker and can be deployed using Docker Compose.

### Services

1. **User Service** provides the ability to register and view info about user.
2. **Messages Service** provides the ability to post and view messages as feed.
3. **Likes Service** provides the ability to like and view likes on messages.

## Running

1. Install [Docker and Docker Compose](https://docs.docker.com/engine/install/).
2. Run `docker-compose up` in the root directory of the project.
3. The services will be available at `http://localhost`.
