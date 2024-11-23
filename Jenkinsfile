pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-1'
        EKS_CLUSTER_NAME = 'flask-app-cluster'
        IMAGE_NAME = 'flask-app'
        ECR_REPOSITORY_URI = '123456789012.dkr.ecr.ap-south-1.amazonaws.com/my-repository'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('AWS CLI Setup') {
            steps {
                script {
                    sh """
                        aws configure set region ${AWS_REGION}
                        aws sts get-caller-identity
                    """
                }
            }
        }

        stage('EKS Authentication') {
            steps {
                script {
                    sh """
                        aws eks --region ${AWS_REGION} update-kubeconfig --name ${EKS_CLUSTER_NAME}
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                        docker build -t ${IMAGE_NAME}:latest .
                    """
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    sh """
                        $(aws ecr get-login --no-include-email --region ${AWS_REGION})
                    """
                    sh """
                        docker tag ${IMAGE_NAME}:latest ${ECR_REPOSITORY_URI}:${IMAGE_NAME}:latest
                        docker push ${ECR_REPOSITORY_URI}:${IMAGE_NAME}:latest
                    """
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    sh """
                        kubectl apply -f kubernetes/deployment.yaml
                        kubectl apply -f kubernetes/service.yaml
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }
        failure {
            echo 'Deployment failed. Check logs for errors.'
        }
    }
}

