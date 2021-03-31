pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
'''
        sh '''python3 manage.py runserver &
'''
        sh '''
echo "============Finish building============"'''
      }
    }

    stage('Tests') {
      steps {
        sh '''sleep 40
'''
        sh '''cd tests

python3 test.py'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''git checkout deploy

git merge main

git push'''
      }
    }

  }
}