pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature1', url: 'https://github.com/arijit0405/jenkins.git'
            }
        }

        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest test_app.py'
            }
        }
    }
}
