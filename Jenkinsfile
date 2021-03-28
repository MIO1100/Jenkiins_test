pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
python3 manage.py runserver &
echo "============Finish building============"
'''
      }
    }

    stage('Tests') {
      steps {
        sh '''cd tests
sleep 40
python3 test.py '''
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