pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
'''
        sh '''nohup python3 manage.py runserver &> /dev/null &

'''
        sh '''
echo "============Finish building============"'''
      }
    }

    stage('Tests') {
      steps {
        sh '''sleep 40
'''
        sh 'python3 tests/test.py'
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