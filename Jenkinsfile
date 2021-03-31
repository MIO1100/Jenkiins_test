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
        sh '''sleep 10
'''
        sh '''xterm -e "python3 tests/test.py && /bin/tcsh" &
'''
      }
    }

    stage('Deploy') {
      steps {
        sh '''git fetch
git remote update

git branch -a

git checkout --track origin/deploy

git merge main

git push'''
      }
    }

  }
}