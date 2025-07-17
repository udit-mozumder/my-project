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
                sh 'python3 -m pip install --user --break-system-packages unittest-xml-reporting'
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
