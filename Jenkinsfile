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
        
        stage('Install SonarQube Scanner') {
            steps {
                sh '''
                    # Install unzip if not available
                    apt-get update && apt-get install -y unzip wget || true
                    
                    # Download and install SonarQube Scanner
                    if [ ! -d "sonar-scanner" ]; then
                        wget -q https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                        unzip -q sonar-scanner-cli-4.8.0.2856-linux.zip
                        mv sonar-scanner-4.8.0.2856-linux sonar-scanner
                    fi
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
