pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-python-app'  // Set your desired Docker image name
        DOCKER_REPO = 'veera1808/my-python-app'  // Replace with your Docker Hub username/repository
        DOCKER_USERNAME = 'veera1808'
        DOCKER_PASSWORD = 'dckr_pat_oatPauXCPRsKrlIb0VsVza4Tjl4'
        
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        /*
        stage('Test') {
            steps {
                script {
                    // Create and activate a virtual environment
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'

                    // Install dependencies
                    sh 'pip install -r requirements.txt'

                    // Run tests (replace with your test command)
                    sh 'pytest'
                }
            }
        }
        */

        stage('Build') {
            steps {
                script {
                    // Install required packages
                    sh 'pip install Flask'

                    // Build Docker image
                    sh "docker build -t $my-python-app ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Tag the Docker image
                    sh "docker tag $my-python-app $veera1808/my-python-app"

                    // Log in to Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'DOCKERHUB_CREDENTIALS_ID', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    }

                    // Push the Docker image to Docker Hub
                  sh "docker push $DOCKER_REPO"

                }
            }
        }
    }

    post {
        always {
            // Clean up: remove the Docker image locally
            script {
                sh "docker rmi $my-python-app"
            }
        }
    }
}
