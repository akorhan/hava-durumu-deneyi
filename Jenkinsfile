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
                withCredentials([usernamePassword(credentialsId: 'github-token', 
                                 passwordVariable: 'GIT_PASSWORD', 
                                 usernameVariable: 'GIT_USERNAME')]) {
                    sh """
                        git config user.email jenkins@ci
                        git config user.name Jenkins
                        git add -A
                        if ! git diff --cached --quiet; then
                            git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/akorhan/hava-durumu-deneyi.git HEAD:master
                        else
                            echo "Degisiklik yok, push atlandi."
                        fi
                    """
                }
            }
        }
    } // <--- Stages bloğunu kapatan parantez eksikti, eklendi.

    post {
        failure {
            echo 'Pipeline basarisiz oldu.'
        }
        success {
            echo 'Pipeline basariyla tamamlandi.'
        }
    }
} // <--- Pipeline ana bloğunu kapatan parantez eksikti, eklendi.
