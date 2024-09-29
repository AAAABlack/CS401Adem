README File:
Project Overview:
This project is a simple calculator application that performs basic operations such as addition, subtraction, multiplication, and division. The application is containerized using Docker and follows a CI/CD setup to ensure quality and continuous deployment.

CI/CD Pipeline Setup:
The CI pipeline uses GitHub Actions to ensure code quality and security. The following steps are implemented in the pipeline:

Linting and Formatting:
Flake8 checks the code for style and syntax issues.
Black ensures code formatting consistency.
Security Scanning:
Bandit performs a security scan to detect potential vulnerabilities in the code.
Unit Testing:
Unittest framework runs all unit tests to ensure correctness.
Branch Rules:
The pipeline is triggered on pushes and pull requests to the master branch.
Docker Setup:
The application can be containerized using Docker, allowing it to run in isolated environments. The Dockerfile is set up to install all necessary dependencies and expose the application on port 5000.

Build Docker Image:

bash
Copy code
docker build -t my-calculator-app .
Run Docker Container:

bash
Copy code
docker run -p 5000:5000 my-calculator-app
Technologies Used:
Python: The core programming language used for building the calculator application.
Flask: Used as a web framework for deploying the app.
GitHub Actions: Used for continuous integration and code quality checks.
Docker: Used for containerizing the application.
