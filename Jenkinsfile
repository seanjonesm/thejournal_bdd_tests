pipeline {
    agent { label 'master' }
    stages {
        stage('git checkout') {
           steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'github_p', url: 'https://github.com/seanjonesm/thejournal_bdd_tests']]])
           }
        }
        stage('run tests') {
            steps {
                 script {
                    try {
                        bat 'behave features\\qatests.feature'
                    } catch (err) {
                        echo err
                    }
                 }
            }
        }
        stage('archive report') {
            steps {
                junit 'reports/*'
            }
        }
    }
}
