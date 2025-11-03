pipeline {
    agent any
    environment {
        PYTHON='C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        APP_TOKEN = credentials("APP_TOKEN")
        
    }
    stages {
        stage('checkout code') {
            steps {
                 checkout scm
            }

        }
        stage('install dependencies') {
            steps {
                 bat "${env.PYTHON} -m pip install -r requirements.txt"
            }

        }
        stage('extract data') {
            steps {
                bat """
                SET TOKEN = %APP_TOKEN% 
                %PYTHON% extract_data.py
                """
            }

        }
  
    }
}
