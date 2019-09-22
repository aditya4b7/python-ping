import paramiko
import sys
import json
import os



def read_json_to_fetch_user_pwd(json_file):
    dct = {}
    with open(json_file) as f:
        data = json.load(f)
    input_list = data['General']['TestType'].split('/')

    for val in input_list:

        if val.strip() in data:
            print(data[val.strip()]['PiIP'])
#            print(data[val.strip()]['UserName'])
#            print(data[val.strip()]['Password'])
            host,port = (data[val.strip()]['PiIP']),22
            transport = paramiko.Transport((host,port))

            username,password = (data[val.strip()]['UserName']),(data[val.strip()]['Password'])
            transport.connect(None,username,password)

            sftp = paramiko.SFTPClient.from_transport(transport)


            file1 = 'server.json'
            destfile1 = 'server.json'
            sftp.put(file1,destfile1)

            file2 = 'icmp.py'
            destfile2 = 'icmp.py'
            sftp.put(file2,destfile2)

            s = paramiko.SSHClient()
            s.load_system_host_keys()
            s.connect(host, port, username, password)
            command = 'python3 icmp.py server.json {0}'.format(host,)
            (stdin, stdout, stderr) = s.exec_command(command)
            for line in stdout.readlines():
              print(line)
            s.close()

            file1 = 'ping-result.log'
            destfile1 = '{0}-ping-result.log'.format(host,)
            sftp.get(file1,destfile1)

            if sftp: sftp.close()
            if transport: transport.close()

        else:
            print ("key not found"),val
    return dct


if __name__ == '__main__':
  try:
      json_file = sys.argv[1]
  except:
      json_file = None
  try:
      input_type = sys.argv[2]
  except:
      input_type = 'All'


  dct = read_json_to_fetch_user_pwd(json_file)
