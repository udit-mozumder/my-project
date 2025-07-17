pipeline {
    agent any

    tools {
        sonarScanner 'SonarScanner'  // Make sure it's configured in Jenkins global tools
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment Check') {
            steps {
                sh '''
                    echo === Environment Check ===
                    python3 --version
                    pip3 --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user unittest-xml-reporting'
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    echo Running unit tests...
                    python3 -m unittest discover -s . -p "*test*.py" -v
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('My SonarQube Server') { // Must match Jenkins → Configure System
                    sh 'sonar-scanner'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished!'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
