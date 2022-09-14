pipeline {
    agent any 
    environment {
        DOCKERHUB_CREDENTIALS = credentials('azurecontainerregistry')
    }
    stages { 

        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login aiccontainerregistry.azurecr.io -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Buildx') {
            steps {  
                sh 'docker buildx create --use --name multiarch-hello'
            }
        }
        stage('push image') {
            steps{
                sh 'docker buildx build --platform linux/arm64 -t aiccontainerregistry.azurecr.io/soundai/test_jenkins -o type=registry .'
            }
        }
}
post {
        always {
            sh 'docker logout'
        }
    }
}
