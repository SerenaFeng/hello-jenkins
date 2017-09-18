pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'start to build hello-jenkins'
                sh './hello_jenkins/builder.sh'
            }
        }
    }
}
