pipeline {
    agent any
    
    stages {
        stage('Check Environment') {
            steps {
                sh '''
                    echo "=== Environment Check ==="
                    python3 --version
                    pip3 --version
                    whoami
                    pwd
                '''
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --user unittest-xml-reporting'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    echo "Running unit tests..."
                    python3 -m unittest discover -s . -p "*test*.py" -v
                '''
            }
        }
        
        stage('Publish Test Results') {
            steps {
                echo "Publishing test results..."
                // Add your test results publishing logic here
                // Example: publishTestResults testResultsPattern: 'test-results.xml'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
