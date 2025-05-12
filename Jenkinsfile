pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature1', url: 'https://github.com/arijit0405/jenkins/tree/feature1/simple_jenkins_pipeline'
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
