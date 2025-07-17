pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/udit-mozumder/my-project.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_main.py'
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/test-results.xml'
            }
        }
    }
}
