pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Clone from Git (optional if you connect to GitHub)
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                // Install dependencies (if any)
                sh 'python --version'
            }
        }

        stage('Run Application') {
            steps {
                // Run your Python script (for demonstration)
                sh 'python app.py < /dev/null || true'  // Accepts no input, avoids Jenkins hanging
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run unit tests
                sh 'python test_app.py'
            }
        }
    }
}
