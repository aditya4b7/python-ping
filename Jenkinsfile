
pipeline {
  agent { label 'master' }
  

    stages {
  
    
    stage('PC1-to-PC2'){
    
		    
		steps {
			  
			  		  
			  sh '''
			      
				  rsync -avh ${WORKSPACE}/PC1 PC1:/home/ --delete-before
				  ssh -t PC1  python ping.py
		  					
				'''
								    
		}
    }
	
 
  }
