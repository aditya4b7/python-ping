import subprocess
import json
import sys
from paramiko import SSHClient
from scp import SCPClient

# empty list that will store ping results
#ping size can be adjusted by changing the number here"(["ping", "-c 2", address])"
with open('pcs.json','r') as f:
        pcs = json.load(f)
        for line in pcs:
            address = line['server'].strip("\n")
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.connect(address)
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())
scp.put('p*', recursive=True, remote_path='/home/pi')
#python3

#python2
#print ping_result
