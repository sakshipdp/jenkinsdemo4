pipeline {
    agent any
    environment {
        PYTHON='C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }
    stages {
        stage('checkout code') {
            steps {
                 checkout scm
            }

        }
        stage('install dependencies') {
            steps {
                 bat '"${env.PYTHON} -m pip install -r requirements.txt"
            }

        }
        stage('extract data') {
            steps {
                 bat "${env.PYTHON} extract_data.py"
            }

        }
  
    }
}
