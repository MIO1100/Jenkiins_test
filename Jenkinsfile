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
        sh '''
if curl -sL --fail  http://127.0.0.1:8000 -o /dev/null; then
    echo "Success"
else
    echo "Fail"
    exit 1
fi'''
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