node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   }

   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'Docker') {
       def app = docker.build("umair841/demo:${commit_id}", '.').push()
     }
   }
}
