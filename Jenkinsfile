
pipeline {
  agent { label 'master' }
  

    stages {
  
    
    stage('PC1-to-PC2'){
    
		    
		steps {
			  
			  		  
			  sh '''
			      
				  rsync -avh ${WORKSPACE}/pc1 pi@192.168.3.2:pc1 --delete-before
				  ssh -t pi@192.168.3.2  python pc1/ping.py
		  					
				'''
								    
		}
    }
	
 
  }
}
	
