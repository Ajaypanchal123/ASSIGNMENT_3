#Features

Web Service: A containerized service that listens on port 5000 and serves a message from the configuration file.
Load Balancer: An NGINX container that acts as a reverse proxy, forwarding requests to the Web Service.
Single Command Setup: The entire project can be started with one command using Docker Compose.

#Practical Workflow

Web Service runs on port 5000 and gets its configuration from the mounted volume.
Load Balancer (NGINX) runs on port 80 and forwards requests to the Web Service.
Both services are connected to a custom Docker network called ajay_network.

#Prerequisites
Before you begin, make sure you have the following installed:
Docker: To Install Docker
Docker Compose: To Install Docker Compose

How to Run the Project

1.Clone or download this project to your local machine and navigate to the project folder:
cd C:/path/to/Assignment_3 

2.Build and start the containers:
docker-compose up --build

3.Access the application:
Web Service: Open your browser and navigate to http://localhost:5000.
Load Balancer: Access the Load Balancer via http://localhost:80.

Folder Structure:

Assignment_3/
├── docker-compose.yml
├── web_service/
│   ├── Dockerfile
│   ├── config/
│   │   └── config.json
│   └── app.py
└── load_balancer/
    └── nginx.conf

Description of Files
docker-compose.yml: The main configuration file that defines services (Web Service and Load Balancer), their configurations, and network setup.
web_service/Dockerfile: Defines the Docker image for the Web Service.
web_service/config/config.json: A configuration file containing settings for the Web Service.
load_balancer/nginx.conf: Custom NGINX configuration for the Load Balancer.

Explanation of Configuration

#Web Service
The Web Service is built from the ./web_service directory and exposes port 5000.
The Web Service gets its configuration from the ./web_service/config directory, allowing you to modify the service's behavior.
The Web Service is connected to the custom ajay_network.

#Load Balancer
The Load Balancer uses the official nginx:latest image.
It listens on port 80 and forwards incoming traffic to the Web Service.
Custom NGINX configuration is mounted from the ./load_balancer/nginx.conf file.
The Load Balancer depends on the Web Service to ensure proper startup order.

#Network
Both the Web Service and Load Balancer are connected to a custom network called ajay_network to facilitate communication between containers.

Stopping the Application
To stop the application and remove the containers, networks, and volumes, use the following command:
docker-compose down

Troubleshooting
Permission Issues: Make sure you have appropriate read/write permissions for the project directory.
Port Conflicts: Ensure that ports 5000 and 80 are not being used by other services.
Build Failures: If you encounter build errors, run docker-compose build separately to see detailed error messages.
