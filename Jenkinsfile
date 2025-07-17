pipeline {
    agent {
        docker {
            image 'python:3.9'
            args '-u root'
        }
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install unittest-xml-reporting'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python -m pytest --junitxml=test-results.xml'
                // or whatever your test command is
            }
        }
        stage('Publish Test Results') {
            steps {
                publishTestResults testResultsPattern: 'test-results.xml'
            }
        }
    }
}

