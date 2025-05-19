pipeline {
    agent any

    environment {
        IMAGE_NAME = "aayush5593/simple-flask-calculator"
        IMAGE_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'dockerhub-id' 
    }

    stages {
        stage('Checkout') {
            steps {
                // Git clone
                git url: 'https://github.com/aayush5593/Simple-Flask-Calculator.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Docker build command
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh "echo 'Add test commands here if any'"
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { env.DOCKERHUB_CREDENTIALS != null }
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKERHUB_CREDENTIALS) {
                        sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

