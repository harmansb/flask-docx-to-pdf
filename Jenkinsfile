pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'harmans0001/flask-docx-to-pdf:latest'  
        AWS_REGION = 'ap-south-1'  
        EKS_CLUSTER_NAME = 'flask-app-cluster'  
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
                        kubectl apply -f kubernetes/deployment.yaml  // Ensure path is correct to your yaml file
                        kubectl apply -f kubernetes/service.yaml
                    '''

                    sh '''
                        kubectl get svc flask-service --output=jsonpath='{.status.loadBalancer.ingress[0].hostname}'
                    '''
                }
            }
        }
    }
}
