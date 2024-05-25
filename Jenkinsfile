pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository
                git branch: 'devops_kubernetes_project', url: 'https://github.com/Budeestar/doc_kub_react_flask.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install frontend dependencies
                    dir('my_app') {
                        sh 'start /b npm install'
                    }
                    // Install backend dependencies
                    dir('flaskbackend') {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the frontend
                    dir('my_app') {
                        sh 'npm run build'
                    }
                    // Additional backend build steps if necessary
                }
            }
        }

        stage('Start Services') {
            steps {
                script {
                    // Start Flask backend
                    dir('flaskbackend') {
                        sh 'python app.py &'
                    }
                    // Start React frontend
                    dir('my_app') {
                        sh 'npm start &'
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
