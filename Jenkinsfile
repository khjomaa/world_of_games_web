pipeline {

    environment {
        registery = "khjomaa/world_of_games_web"
        registryCredintals = 'DockerHub'
        dockerImage = ''
    }

    agent any

    triggers {
        pollSCM '*/2 * * * *'
    }

    stages {
        stage('Checkout') {
            steps {
                git "https://github.com/khjomaa/world_of_games_web.git"
            }
        }
        stage("Build") {
            steps {
                script {
                    dockerImage = docker.build registery + ":$BUILD_NUMBER"
                }
            }
        }
        stage("Run") {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage("Test") {
            steps {
                sh 'docker exec wog python tests/e2e.py'
            }
        }
        stage("Finalize") {
            steps {
                script {
                    docker.withRegistry( '', registryCredintals ) {
                        dockerImage.push()
                    }
                }
                sh 'docker-compose down;docker rmi $(docker images -q)'
            }
        }
    }
}