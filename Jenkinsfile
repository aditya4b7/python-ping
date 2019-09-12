#!/usr/bin/groovy

def performsfsDeployment(String share) {
    stage("${share}") {
                sh "scp -r p* pi@${share}:"
                sh "ssh pi@${share} python ping.py "
                sh "scp -r pi@${share}:ping-result.log ."
                sh "mv ping-result.log ${share}-ping-result.log"
        }

}


node('master') {

        stage('Checkout') {
                checkout scm
        }

        def rootDir = pwd()
        println "rootDir :: ${rootDir}"

        // Read required jenkins workflow configuration values.
        def config = readJSON file:'pcs.json'


                stage('ping-test') {
                                                def sfs = [:]
                                                for (share in config.server) {
                                                        performsfsDeployment(share)

                                                }

                        }

                   stage('Archive') {
                                archiveArtifacts artifacts: '*-ping-result.log', onlyIfSuccessful: true
                        }



}

