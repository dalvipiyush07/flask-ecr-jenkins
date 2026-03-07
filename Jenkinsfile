pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
        REPOSITORY_URI = '528471666387.dkr.ecr.ap-south-1.amazonaws.com/flask-app-repo'
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/dalvipiyush07/flask-ecr-jenkins.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Tag Image') {
            steps {
                sh 'docker tag flask-app:latest ${REPOSITORY_URI}:latest'
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-ecr-credentials']]) {
                    sh '''
                    aws ecr get-login-password --region ap-south-1 | \
                    docker login --username AWS --password-stdin 528471666387.dkr.ecr.ap-south-1.amazonaws.com
                    '''
                }
            }
        }

        stage('Push Image to ECR') {
            steps {
                sh 'docker push ${REPOSITORY_URI}:latest'
            }
        }
    }

    post {
        success {
            echo 'Docker Image Successfully Pushed to Amazon ECR'
        }

        failure {
            echo 'Pipeline Failed. Check Jenkins Logs.'
        }
    }
}
