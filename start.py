import os
from subprocess import Popen, PIPE


(stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-T','fields','-e','gtp.seq_number','-Y','e212.imsi == 204043740503899'], stdout=PIPE).communicate()

tmp = stdout

a = tmp.splitlines()

 


#tshark -r /home/pi/tshark/test.pcapng -t ud -Y "gtp.seq_number == 0x0000f205"


for i in a:
        t = "gtp.seq_number == " + i

        (stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-Y',t], stdout=PIPE).communicate()
        print stdout



