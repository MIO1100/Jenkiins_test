pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
'''
        sh '''python3 manage.py runserver &> /dev/null &

'''
        sh '''
echo "============Finish building============"'''
      }
    }

    stage('Tests') {
      steps {
        sh '''sleep 40
'''
        sh '''#!/bin/bash
cd tests
python3 test.py'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''cd ..

git checkout deploy

git merge main

git push'''
      }
    }

  }
}