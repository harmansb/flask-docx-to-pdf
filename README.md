# Flask DOCX to PDF Converter

A simple web application built using Flask that allows users to upload DOCX files and convert them into PDF files. This project is containerized using Docker and deployed on AWS EKS with Kubernetes for scalability.

## Features
- Upload DOCX files.
- Convert DOCX files to PDF.
- REST API for easy integration.

## Technologies Used
- **Flask**: A lightweight web framework for Python.
- **Docker**: Containerization of the Flask application.
- **AWS EKS**: Elastic Kubernetes Service for managing and scaling the Kubernetes clusters.
- **Kubernetes**: Orchestrates containerized applications.
- **Docker Hub**: For storing the Docker image.
- **AWS EC2**: For managing and provisioning resources.

## Prerequisites

Before running the application locally or deploying it, ensure that you have the following installed:

1. **Docker**: To containerize the application.
   - [Install Docker](https://docs.docker.com/get-docker/)
   
2. **AWS CLI**: To manage AWS resources.
   - [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

3. **eksctl**: CLI tool for creating and managing EKS clusters.
   - [Install eksctl](https://eksctl.io/)

4. **kubectl**: Kubernetes CLI tool for interacting with your EKS cluster.
   - [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/flask-docx-to-pdf.git
cd flask-docx-to-pdf
