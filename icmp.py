import paramiko
import sys
import json
import os
import subprocess


def read_json_to_fetch_user_pwd(json_file):
    ping_result = "\n\n"
    dct = {}
    with open(json_file) as f:
        data = json.load(f)
    input_list = data['General']['TestType'].split('/')

    for val in input_list:

        if val.strip() in data:
            host = (data[val.strip()]['PiIP'])

            res = subprocess.call(["ping", "-c 5", host])
            if res == 0:
                ping_result = ping_result + "ping to " + host + " OK" + " \n"
            elif res == 2:
                ping_result = ping_result + "no response from " + host + " \n"
            else:
                ping_result = ping_result + "ping to " + host + " failed!" + " \n"

te = open("ping-result.log",'a')

class Unbuffered:

   def __init__(self, stream):

       self.stream = stream

   def write(self, data):

       self.stream.write(data)
       self.stream.flush()
       te.write(data)    # Write the data of stdout here to a text file as well



       sys.stdout=Unbuffered(sys.stdout)

       print (ping_result)

#      else:
#       print ("key not found"),val
#    return dct


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
