pipeline {
    agent any 
    environment {
        DOCKERHUB_CREDENTIALS = credentials('azurecontainerregistry')
    }
    stages { 

        stage('Build docker image') {
            steps {  
                sh 'docker build -t aiccontainerregistry.azurecr.io/soundai/test_jenkins:latest .'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push aiccontainerregistry.azurecr.io/soundai/test_jenkins:latest'
            }
        }
}
post {
        always {
            sh 'docker logout'
        }
    }
}
