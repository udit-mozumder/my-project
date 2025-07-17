pipeline {
    agent {
        docker {
            image 'python:3.9'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/udit-mozumder/my-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install unittest-xml-reporting'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python -m xmlrunner discover -s . -p "test_*.py" -o test-reports'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-reports/*.xml'
            }
        }
    }
}
