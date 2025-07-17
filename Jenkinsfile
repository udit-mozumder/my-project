pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user unittest-xml-reporting'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m xmlrunner discover -s . -p "*_test.py" -o test-reports || true'
            }
        }
        stage('Publish Test Results') {
            steps {
                junit 'test-reports/*.xml'
            }
        }
    }
}

