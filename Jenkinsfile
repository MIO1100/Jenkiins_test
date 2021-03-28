pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
pip3 install django requests 
python3 manage.py runserver &
sleep 30
echo "============Finish building============"
'''
      }
    }

    stage('Tests') {
      steps {
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