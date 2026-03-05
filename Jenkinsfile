pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    ${VENV_DIR}/bin/pip install --upgrade pip
                    ${VENV_DIR}/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '${VENV_DIR}/bin/python weather.py'
            }
        }

        stage('Push') {
            steps {
                sh '''
                    git config user.email "jenkins@ci"
                    git config user.name "Jenkins"
                    git add -A
                    git diff --cached --quiet || git commit -m "ci: automated build [skip ci]"
                    git push origin HEAD:master
                '''
            }
        }
    }

    post {
        failure {
            echo 'Pipeline basarisiz oldu. Push adimi atildi.'
        }
        success {
            echo 'Pipeline basariyla tamamlandi.'
        }
    }
}
