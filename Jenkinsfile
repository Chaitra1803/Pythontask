pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS_ID = 'dockerhub-token'
        DOCKER_IMAGE = 'my-python-app'
        DOCKER_USERNAME = 'veera1808'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "docker tag $DOCKER_IMAGE $DOCKER_USERNAME/$DOCKER_IMAGE"
                    withCredentials([string(credentialsId: DOCKERHUB_CREDENTIALS_ID, variable: 'DOCKER_TOKEN')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_TOKEN"
                    }
                    sh "docker push $DOCKER_USERNAME/$DOCKER_IMAGE"
                }
            }
        }
    }
}
