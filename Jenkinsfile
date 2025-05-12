pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python test_app.py'
            }
        }
    }
}
