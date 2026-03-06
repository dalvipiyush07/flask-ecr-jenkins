pipeline {
    agent any

    environment {
        // Your AWS region where the ECR repository exists
        AWS_DEFAULT_REGION = 'ap-south-1'

        // Full ECR repository URI
        REPOSITORY_URI = '528471666387.dkr.ecr.ap-south-1.amazonaws.com/flask-app-repo'

        // ID of the AWS credentials stored in Jenkins
        AWS_CREDS = 'aws-ecr-credentials'
    }

    stages {

        stage('Checkout Code') {
            steps {
                // Clone the source code from GitHub
                git branch: 'main',
                    url: 'https://github.com/dalvipiyush07/flask-ecr-jenkins.git'
                // NOTE: If the repository is public, credentials are not required.
                // If the repository is private, you must add GitHub credentials in Jenkins.
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image and tag it as latest
                    def appImage = docker.build("${REPOSITORY_URI}:latest")
                }
            }
        }

        stage('Push to ECR') {
            steps {
                script {
                    // Authenticate to Amazon ECR and push the image
                    docker.withRegistry("https://${REPOSITORY_URI}", "ecr:${AWS_DEFAULT_REGION}:${AWS_CREDS}") {
                        sh "docker push ${REPOSITORY_URI}:latest"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image successfully pushed to Amazon ECR!'
            echo "Image URI: ${REPOSITORY_URI}:latest"
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
