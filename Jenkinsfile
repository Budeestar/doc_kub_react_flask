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
                        bat 'start /B npm install'
                    }
                    // Install backend dependencies
                    dir('flaskbackend') {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the frontend
                    dir('my_app') {
                        bat 'npm run build'
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
                        bat 'python app.py &'
                    }
                    // Start React frontend
                    dir('my_app') {
                        bat 'npm start &'
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
