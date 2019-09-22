import paramiko
import sys
import json
import os
import subprocess


def read_json_to_fetch_user_pwd(json_file,input_type):
    ping_result = "\n\n"
    dct = {}
    with open(json_file) as f:
        data = json.load(f)
    input_list = data['General']['TestType'].split('/')

    for val in input_list:

        if val.strip() in data:
            host = (data[val.strip()]['PiIP'])
            print(input_type,host)
            if host == input_type:
                continue
            else:
                
                res = subprocess.call(["ping", "-c 5", host])
                if res == 0:
                    ping_result = ping_result + "ping to " + host + " OK" + " \n"
                    print (ping_result)
                elif res == 2:
                    ping_result = ping_result + "no response from " + host + " \n"
                    print (ping_result)
                else:
                    ping_result = ping_result + "ping to " + host + " failed!" + " \n"
                    print (ping_result)



# class Unbuffered:

#    def __init__(self, stream):

#        self.stream = stream

#    def write(self):

# #       self.stream.write(data)
# #       self.stream.flush()
#        te = open("ping-result.log",'a')
#        te.write(self.stream)    # Write the data of stdout here to a text file as well
#        te.close()


       

#        print (ping_result)



class Unbuffered:



    def __init__(self, stream):

        self.stream = stream

    def write(self, data):

       self.stream.write(data)
#       self.stream.flush()
       te = open("ping-result.log",'a')
       te.write(data)
       te.write('\n')    # Write the data of stdout here to a text file as well
       te.close()


sys.stdout=Unbuffered(sys.stdout)

#print (ping_result)
   
    

if __name__ == '__main__':
  try:
      json_file = sys.argv[1]
  except:
      json_file = None
  try:
      input_type = sys.argv[2]
  except:
      input_type = 'All'

dct = read_json_to_fetch_user_pwd(json_file,input_type)
