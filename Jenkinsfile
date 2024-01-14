pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-token'
        DOCKER_IMAGE = 'my-python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Clone the repository
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Add your testing steps here if applicable
                    // For example: sh 'python -m unittest discover -s tests'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    sh "docker tag $DOCKER_IMAGE veera1808/$DOCKER_IMAGE"
                    withCredentials([string(credentialsId: DOCKERHUB_CREDENTIALS_ID, variable: 'DOCKER_TOKEN')]) {
                        sh "docker login -u veera1808 -p $DOCKER_TOKEN"
                    }
                    sh "docker push veera1808/$DOCKER_IMAGE"
                }
            }
        }
    }
}
