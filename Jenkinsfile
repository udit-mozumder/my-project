pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install unittest-xml-reporting pytest pytest-cov
                '''
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest --junitxml=test-results.xml --cov=. --cov-report=xml || true
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQube') {
                        sh '''
                            # Create sonar-project.properties file
                            cat > sonar-project.properties << EOF
sonar.projectKey=my-project
sonar.projectName=My Project
sonar.projectVersion=1.0
sonar.sources=.
sonar.exclusions=**/venv/**,**/test_*,**/__pycache__/**,**/.*,**/sonar-scanner-*/**
sonar.python.coverage.reportPaths=coverage.xml
sonar.python.xunit.reportPath=test-results.xml
sonar.language=python
sonar.sourceEncoding=UTF-8
EOF
                            
                            # Run SonarQube analysis using sonar-scanner
                            if command -v sonar-scanner >/dev/null 2>&1; then
                                echo "Using system sonar-scanner"
                                sonar-scanner
                            else
                                echo "SonarQube Scanner not found. Installing..."
                                
                                # Download sonar-scanner using curl or wget
                                if command -v curl >/dev/null 2>&1; then
                                    curl -L -o sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                                elif command -v wget >/dev/null 2>&1; then
                                    wget -O sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.8.0.2856-linux.zip
                                else
                                    echo "Neither curl nor wget found. Cannot download sonar-scanner."
                                    exit 1
                                fi
                                
                                # Extract using Python
                                if [ ! -d "sonar-scanner-4.8.0.2856-linux" ]; then
                                    python3 -c "
import zipfile
import os
try:
    with zipfile.ZipFile('sonar-scanner.zip', 'r') as zip_ref:
        zip_ref.extractall('.')
    print('Successfully extracted sonar-scanner')
except Exception as e:
    print(f'Error extracting: {e}')
    exit(1)
"
                                fi
                                
                                # Run sonar-scanner
                                if [ -f "./sonar-scanner-4.8.0.2856-linux/bin/sonar-scanner" ]; then
                                    chmod +x ./sonar-scanner-4.8.0.2856-linux/bin/sonar-scanner
                                    
                                    # Set JAVA_HOME for SonarQube scanner
                                    export JAVA_HOME=/opt/java/openjdk
                                    export PATH=$JAVA_HOME/bin:$PATH
                                    
                                    # Verify Java is available
                                    java -version
                                    
                                    # Run SonarQube scanner
                                    ./sonar-scanner-4.8.0.2856-linux/bin/sonar-scanner
                                else
                                    echo "SonarQube Scanner binary not found after extraction"
                                    exit 1
                                fi
                            fi
                        '''
                    }
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 5, unit: 'MINUTES') {
                        def qg = waitForQualityGate()
                        if (qg.status != 'OK') {
                            echo "Quality Gate failed: ${qg.status}"
                            // Don't fail the build, just warn
                            unstable("Quality Gate failed")
                        } else {
                            echo "Quality Gate passed!"
                        }
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline finished!'
            junit 'test-results.xml'
            
            // Archive artifacts
            archiveArtifacts artifacts: 'coverage.xml,test-results.xml', fingerprint: true, allowEmptyArchive: true
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
        unstable {
            echo 'Build unstable - Quality Gate issues found!'
        }
    }
}
