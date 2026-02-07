# Project Nexus – Movie Recommendation Backend (ProDev BE)

This project is a production-ready backend system for a movie recommendation application.  
It follows twelve-factor app principles, uses Docker for deployment, and integrates external
services for scalability and performance.

---

## Overview

The Movie Recommendation Backend provides RESTful APIs for retrieving trending movies,
managing user authentication, and allowing users to save their favorite movies.
The system emphasizes clean architecture, performance optimization, and clear API documentation.

---

## Features

- Fetch trending movies using the TMDb API
- JWT-based user authentication
- Save and retrieve user favorite movies
- Redis caching for high-performance API responses
- Swagger (OpenAPI) documentation for all endpoints

---

## Technologies Used

- Django & Django REST Framework
- PostgreSQL
- Redis
- TMDb API
- JWT Authentication
- Swagger (drf-yasg)
- Docker & Docker Compose
- Nginx (reverse proxy)

---

## System Architecture

- Django REST API handles business logic
- PostgreSQL stores persistent application data
- Redis caches frequently accessed movie data
- TMDb provides external movie information
- Nginx proxies requests to Gunicorn

---

## Running the Application (Docker – Recommended)

The application is fully containerized and can be run using Docker Compose.

### Prerequisites
- Docker
- Docker Compose
- TMDb API Key

### Start the Application

```bash
docker compose -f docker-compose-nexus.yaml up --build
```