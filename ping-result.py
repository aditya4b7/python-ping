import subprocess
import json
import sys
# empty list that will store ping results
ping_result = "\n\n"
#ping size can be adjusted by changing the number here"(["ping", "-c 2", address])"
with open('pcs.json','r') as f:
    pcs = json.load(f)
    for line in pcs:
        address = line['server'].strip("\n")

        res = subprocess.call(["ping", "-c 5", address])
        if res == 0:
            ping_result = ping_result + "ping to " + address + " OK" + " \n"
        elif res == 2:
            ping_result = ping_result + "no response from " + address + " \n"
        else:
            ping_result = ping_result + "ping to " + address + " failed!" + " \n"

#python3



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

print (ping_result)
#python2
#print ping_result
