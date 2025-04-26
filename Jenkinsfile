# Define the Groovy Jenkins pipeline as a multi-line string
jenkinsfile_content = '''pipeline {
    agent any

    environment {
        EC2_SERVER = "ec2-user@http://18.116.19.31/"  // Amazon Linux default user is ec2-user
        EC2_PRIVATE_KEY = credentials('your-ssh-credential-id')  // The SSH private key stored in Jenkins credentials store
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/shubhamvraut/fastapi.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'  // Run only for 'main' branch
            }
            steps {
                // Use ssh-agent to inject the private key
                sshagent(credentials: ['your-ssh-credential-id']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no $EC2_SERVER "
                            cd /home/ec2-user/your-repo &&
                            git pull origin main &&
                            docker-compose up -d
                        "
                    '''
                }
            }
        }
    }
}
'''

# Write the content to a 'Jenkinsfile' in the current directory
with open('Jenkinsfile', 'w') as file:
    file.write(jenkinsfile_content)

print("Jenkinsfile has been generated successfully!")
