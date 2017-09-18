pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'start to build hello-jenkins'
                sh './hello_jenkins/builder.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'start to test hello-jenkins'
                sh './hello_jenkins/builder.sh'
            }
        }
        stage('Deploy') {
            steps {
                echo 'start to deploy hello-jenkins'
                sh './hello_jenkins/builder.sh'
            }
        }
    }
}
