# Django-hubspot-integration
This project integrates Django with HubSpot to manage CRM functionalities. It provides a seamless way to synchronize data between your Django application and HubSpot.

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

This will build and run the Docker containers required for the project. Once the containers are up and running, you can access the application at `http://localhost:8000`.

### Stop the Containers

To stop the containers, use the following command:

```sh
docker-compose down
```

### Environment Variables

Make sure to create a `.env` file in the root directory of the project and add the following variables:

```
HUBSPOT_API_KEY=YOUR_HUBSPOT_API_KEY
SECRET_KEY=YOUR_SECRET_KEY
```

Replace `YOUR_HUBSPOT_API_KEY` with your actual HubSpot API key and `YOUR_SECRET_KEY` with your own secret key.

