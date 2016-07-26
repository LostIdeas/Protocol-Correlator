#import os
#filters=[f1,f2,...]
#input = 'abc.cap'
#output = 'xyz.cap'
#for f in filters
#   cmd = 'tshark -r ' + input + ' -R ' + f  + ' -w ' + output
#   os.system(cmd)

import os
from subprocess import Popen, PIPE



#cmd = 'tshark -r /home/pi/tshark/* -t ud -T fields -e gtp.seq_number -Y "e212.imsi == 204043740503899"' 
#stdout=os.system(cmd)


#print "sasa"
#print stdout

(stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-T','fields','-e','gtp.seq_number','-Y','e212.imsi == 204043740503899'], stdout=PIPE).communicate()
print stdout[0:10]

print stdout[10:21]

#(stdout, stderr) = Popen(["cat","foo.txt"], stdout=PIPE).communicate()
