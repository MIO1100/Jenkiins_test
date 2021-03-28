pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''echo "============Start building============"
pip3 install django
python3 manage.py runserver &
sleep 10
echo "============Finish building============"
'''
      }
    }

    stage('Tests') {
      steps {
        sh '''cd tests
python test.py'''
      }
    }

  }
}