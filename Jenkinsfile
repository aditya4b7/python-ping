
pipeline {
  agent { label 'master' }
  

    stages {
  
    
    stage('PC1-to-PC2'){
    
		    
		steps {
			  
			  		  
			  sh '''
			      
				  scp -r ${WORKSPACE}/pc1/* pi@192.168.3.2: 			  		 ssh -t pi@192.168.3.2  python ping.py
		  					
				'''
								    
		}
    }
	
      stage('PC2-to-PC1'){


                steps {


                          sh '''

                                  scp -r ${WORKSPACE}/pc2/* pi@192.168.3.3:                                      ssh -t pi@192.168.3.3  python ping.py

                                '''

                }
    }

     stage('Jen-PC1-PC2'){


                steps {


                          sh 'python ping.py'

                }
    }
 
  }

}
