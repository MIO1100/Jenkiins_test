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

	environment {
                GIT_AUTH = credentials('baab9e52-24fb-43fc-ad9a-d5ea0072af32')
            }

      steps {
        sh '''cd ..

git checkout deploy

git merge main

                    git config --local credential.helper "!f() { echo username=\\$GIT_AUTH_USR; echo password=\\$GIT_AUTH_PSW; }; f"
                    git push origin HEAD:$TARGET_BRANC
                ''')
            }
      }
    }

  }
}
