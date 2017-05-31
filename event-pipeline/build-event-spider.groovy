pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                sh 'pwd > workspace'
                echo "$workspace"
            }
        }
    }
}