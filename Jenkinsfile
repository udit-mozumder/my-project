pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'
        }
    }
    
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
                    # Update package list and install required tools
                    apt-get update
                    apt-get install -y wget unzip
                    
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
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                            . venv/bin/activate
                            
                            ./sonar-scanner/bin/sonar-scanner \
                                -Dsonar.projectKey=my-project \
                                -Dsonar.projectName="My Project" \
                                -Dsonar.projectVersion=1.0 \
                                -Dsonar.sources=. \
                                -Dsonar.exclusions="**/venv/**,**/test_*,**/sonar-scanner/**" \
                                -Dsonar.python.coverage.reportPaths=coverage.xml \
                                -Dsonar.python.xunit.reportPath=test-results.xml \
                                -Dsonar.language=python
                        '''
                    }
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 5, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            error "Pipeline aborted due to quality gate failure: ${qg.status}"
                        }
                    }
                }
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
