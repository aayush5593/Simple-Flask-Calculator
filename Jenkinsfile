pipeline {
    agent any

    environment {
        IMAGE_NAME = "aayushhhsharma/simple-flask-calculator"
        IMAGE_TAG = "latest"
        DOCKERHUB_CREDENTIALS = 'DockerHub' 
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
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
        stage('Run Container') {
        steps {
        script {
            def containerId = sh(script: 'docker run -d -p 8080:8081 --name flask-container aayushhhsharma/simple-flask-calculator:latest', returnStdout: true).trim()
            echo "Container is running with ID: ${containerId}"
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

