# Django-hubspot-integration
This project integrates an external advanced CRM API system of HubSpot with Django Rest Framework. It provides a seamless way to synchronize data between your Django application and HubSpot.

## Features

- Sync contacts between Django and HubSpot
- Manage HubSpot deals from Django
- Automated workflows and triggers

## Prerequisites

- Docker
- Docker Compose

## Getting Started

### Clone the Repository

```sh
git clone https://github.com/ATOUIYakoub/Django-hubspot-integration.git
cd Django-hubspot-integration
```

### Build and Run with Docker

```sh
docker-compose up --build
```

This will build and run the Docker containers required for the project. Once the containers are up and running, you can access the application at SWAGGER `http://localhost:8000/api/schema/docs`.

### Stop the Containers

To stop the containers, use the following command:

```sh
docker-compose down
```

### Environment Variables

Make sure to create a `.env` file in the root directory of the project and add the following variables:

```properties
SECRET_KEY=YOUR_SECRET_KEY
HUBSPOT_CLIENT_SECRET=YOUR_HUBSPOT_CLIENT_SECRET
HUBSPOT_REDIRECT_URI=http://localhost:8000/oauth/callback
HUBSPOT_ACCESS_TOKEN=YOUR_HUBSPOT_ACCESS_TOKEN
```

Replace `YOUR_SECRET_KEY` with your own secret key, `YOUR_HUBSPOT_CLIENT_SECRET` with your HubSpot client secret, `http://localhost:8000/oauth/callback` with your HubSpot redirect URI, and `YOUR_HUBSPOT_ACCESS_TOKEN` with your HubSpot access token.
