pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-docx-to-pdf:latest'
        AWS_REGION = 'us-east-1'  // Modify to your region
        EKS_CLUSTER_NAME = 'flask-app-cluster'  // Modify to your EKS cluster name
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy to AWS EKS') {
            steps {
                script {
                    sh '''
                        aws eks --region ${AWS_REGION} update-kubeconfig --name ${EKS_CLUSTER_NAME}
                    '''

                    sh '''
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                    '''

                    sh '''
                        kubectl get svc flask-service --output=jsonpath='{.status.loadBalancer.ingress[0].hostname}'
                    '''
                }
            }
        }
    }
}
