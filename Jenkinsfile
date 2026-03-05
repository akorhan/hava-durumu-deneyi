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
        // 'github-token' senin Jenkins'e eklediğin credential ID'si olmalı
        withCredentials([usernamePassword(credentialsId: 'github-token', 
                         passwordVariable: 'GIT_PASSWORD', 
                         usernameVariable: 'GIT_USERNAME')]) {
            sh """
                git config user.email jenkins@ci
                git config user.name Jenkins
                git add -A
                # Değişiklik varsa pushla
                if ! git diff --cached --quiet; then
                    # URL'ye token enjekte ediyoruz
                    git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/akorhan/hava-durumu-deneyi.git HEAD:master
                else
                    echo "Degisiklik yok, push atlandi."
                fi
            """
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
