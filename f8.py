pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                script {
                    docker.build('sample-web-app')
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                echo 'Running Docker Container...'
                script {
                    docker.image('sample-web-app').run('-d -p 8080:8080')
                }
            }
        }
    }
}
new file
