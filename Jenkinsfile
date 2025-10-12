pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *') // Polls every 2 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout([$class: 'GitSCM', 
                          branches: [[name: 'b1']], 
                          userRemoteConfigs: [[url: 'https://github.com/dxtprashant07/newgit.git']]])
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
                // Example: simulate build
                sh 'echo "Build successful"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example: simulate test
                sh 'echo "Tests passed"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Example: simulate deployment
                sh 'echo "Deployment done"'
            }
        }
    }
}
