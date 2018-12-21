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
                   bat 'behave features\\basic_tests.feature'
                   }
            }
        }

     post { 
        always { 
          junit 'reports/*'  
        }
        }
}
