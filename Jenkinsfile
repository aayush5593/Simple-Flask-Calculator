pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/aayush5593/Simple-Flask-Calculator.git', branch: 'main'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
    }
}
