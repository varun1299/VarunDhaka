pipeline {
	agent any
	triggers {
		cron('H H * * *') // Mid-night build
	}
	// can also use cron ('0 0 * * *') for midnight builds.
	//To allow periodically scheduled tasks to produce even load on the system, the symbol H (for “hash”) should be used wherever possible.
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

