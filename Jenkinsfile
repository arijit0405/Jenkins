pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Python Dependencies') {
            steps {
                bat 'pip install pytest'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python simple_jenkins_pipeline/app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest simple_jenkins_pipeline/app_test.py'
            }
        }
    }

    post {
        success {
            echo '✅ Build completed successfully!'
        }
        failure {
            echo '❌ Build failed.'
        }
    }
}
