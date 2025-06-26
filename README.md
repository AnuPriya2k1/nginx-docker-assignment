# 🚀 Nginx Reverse Proxy + Docker Compose Assignment

This project sets up a full Docker Compose-based stack with an **Nginx reverse proxy** routing to two services:

- ✅ **Service 1**: A simple **Golang** web app available at `/service1`
- ✅ **Service 2**: A basic **Flask (Python)** app available at `/service2`

---

## 📦 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/AnuPriya2k1/nginx-docker-assignment.git
cd nginx-docker-assignment
## Build and start containers
docker-compose up --build
This will:

    Build and run Nginx as a reverse proxy on port 80

    Build and run:

        Service 1 on port 8001

        Service 2 on port 8002
## Access the Services in Browser
### Routing Work
##Nginx listens on port 80 and uses path-based routing to forward requests to backend services.

events {}

http {
    server {
        listen 80;

        location /service1/ {
            rewrite ^/service1(/.*)$ $1 break;
            proxy_pass http://service1:8001/;
        }

        location /service2/ {
            rewrite ^/service2(/.*)$ $1 break;
            proxy_pass http://service2:8002/;
        }
    }
}

## Basic health checks are configured inside docker-compose.yml

  service1:
    ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8001/"]
      interval: 10s
      timeout: 3s
      retries: 3

  service2:
    ...
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8002/"]
      interval: 10s
      timeout: 3s
      retries: 3
## You can check container health by
docker ps

## Nginx logs are linked to standard output and can be viewed using
docker-compose logs nginx

## Folder structure
Nginx-docker-assignment/
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
├── service1/
│   └── main.go
├── service2/
│   └── app.py
└── README.md

