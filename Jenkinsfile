pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'start to build hello-jenkins'
                bash ./hello_jenkins/builder.sh
            }
        }
    }
}
