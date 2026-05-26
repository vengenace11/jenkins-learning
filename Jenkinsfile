pipeline {
    agent any

    stages {
        stage('Check files') {
            steps {
                sh 'ls -la'
                sh 'ls -la data'
            }
        }

        stage('Install Python packages') {
            steps {
                sh 'python3 -m pip install --user -r requirements.txt'
            }
        }

        stage('Run data pipeline') {
            steps {
                sh 'python3 pipeline.py'
            }
        }

        stage('Show output') {
            steps {
                sh 'cat output/sales_summary.csv'
            }
        }
    }
}
