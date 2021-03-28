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
curl -Is http://127.0.0.1:8000 | head -1'''
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