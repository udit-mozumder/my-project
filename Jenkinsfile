pipeline {
    agent any

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
                sh 'python3 test_main.py'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-reports/*.xml'
            }
        }
    }
}

