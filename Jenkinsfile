pipeline {
    agent any
    environment {
        IMAGE_NAME = 'ilanhamoy/Wog_app_image'
        CONTAINER_NAME = 'Wog_app_container'
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(env.IMAGE_NAME)
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d --name ${env.CONTAINER_NAME} -p 5000:5000 ${env.IMAGE_NAME}"
                }
            }
        }
        stage('Test Application') {
            steps {
                script {
                    // Ensure Python and necessary dependencies are setup if needed
                    def result = sh(script: 'python test/e2e.py', returnStatus: true)
                    if (result != 0) {
                        error('End-to-end tests failed!')
                    }
                }
            }
        }
        stage('Cleanup and Push') {
            steps {
                script {
                    sh "docker stop ${env.CONTAINER_NAME}"
                    sh "docker rm ${env.CONTAINER_NAME}"
                    sh "docker push ${env.IMAGE_NAME}"
                }
            }
        }
    }
    post {
        always {
            // Cleanup Docker image locally after tasks
            sh "docker rmi ${env.IMAGE_NAME}"
        }
    }
}
