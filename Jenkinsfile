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
                sh '''
                    # Create virtual environment if it doesn't exist
                    if [ ! -d "/var/jenkins_home/venv" ]; then
                        python3 -m venv /var/jenkins_home/venv
                    fi
                    
                    # Activate virtual environment and install packages
                    source /var/jenkins_home/venv/bin/activate
                    pip install unittest-xml-reporting
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    echo "Running unit tests..."
                    # Activate virtual environment
                    source /var/jenkins_home/venv/bin/activate
                    python -m unittest discover -s . -p "*test*.py" -v
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
