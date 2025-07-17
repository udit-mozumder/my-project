pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install unittest-xml-reporting pytest pytest-cov
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest --junitxml=test-results.xml --cov=. --cov-report=xml || true
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished!'
            junit 'test-results.xml'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

