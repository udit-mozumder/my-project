pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install unittest-xml-reporting'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m xmlrunner discover -s . -p "*_test.py" -o test-reports'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-reports/*.xml'
            }
        }
    }
}
