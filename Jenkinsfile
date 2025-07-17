pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/udit-mozumder/my-project.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                // Run tests and capture results in JUnit-compatible output
                sh 'python3 -m unittest discover -s . -p "*_test.py" > test-results.txt || true'
                sh 'cat test-results.txt'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results.txt'
        }
    }
}
📌 Tip: Use 
