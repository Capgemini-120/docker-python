pipeline {
  agent any 
  stages {
     stage(checkout) {
        steps {
          echo "Hello this is sample program"
        }
     }
  }
}
