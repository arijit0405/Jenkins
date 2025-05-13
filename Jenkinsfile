pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run App') {
            steps {
                bat 'python simple_jenkins_pipeline/app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python simple_jenkins_pipeline/app_test.py'
            }
        }
    }

    post {
        success {
            script {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    def repo = "arijit0405/jenkins"
                    def featureBranch = "feature1"
                    def mainBranch = "main"
                    def prTitle = "Auto PR from ${featureBranch} to ${mainBranch}"

                    sh """
                    curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
                    -H "Accept: application/vnd.github+json" \
                    https://api.github.com/repos/${repo}/pulls \
                    -d '{
                        "title": "${prTitle}",
                        "head": "${featureBranch}",
                        "base": "${mainBranch}",
                        "body": "Automated PR from Jenkins on successful build"
                    }'
                    """
                }
            }
        }
    }
}
