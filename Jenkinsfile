pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
'''
        sh ' python3 run.py '
        sh '''
echo "============Finish building============"'''
      }
    }

    stage('Tests') {
      steps {
        sh 'sleep 10'
      }
    }

    stage('Deploy') {
      environment {
        GIT_AUTH = credentials('0fd028b5-abd2-4320-91ed-3c6a868b9019')
      }
      steps {
        sh '''
git checkout deploy

git merge main

git config --local credential.helper "!f() { echo username=\\$GIT_AUTH_USR; echo password=\\$GIT_AUTH_PSW; }; f"

git push --set-upstream origin deploy

'''
      }
    }

  }
}