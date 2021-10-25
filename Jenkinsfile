pipeline {
	agent any
	//agent { docker { image 'python:3.7.2' } }
 	stages {
 		stage("Compile") {
 			steps {
 				echo "python compile done"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python test.py"
 			}
 		}
 	}
}

