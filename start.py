import os
from subprocess import Popen, PIPE


(stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-T','fields','-e','gtp.seq_number','-Y','e212.imsi == 204043740503899'], stdout=PIPE).communicate()

tmp = stdout

a = tmp.splitlines()

 


#tshark -r /home/pi/tshark/test.pcapng -t ud -Y "gtp.seq_number == 0x0000f205"


#for i in a:
for j,i in enumerate(a):
        t = "gtp.seq_number == " + i
        s = "/home/pi/tshark/"+str(j)+".pcap"
        
        #(stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-Y',t], stdout=PIPE).communicate()
        (stdout, stderr) = Popen(['tshark','-r','/home/pi/tshark/test.pcapng','-t','ud','-w',s,'-Y',t], stdout=PIPE).communicate()
for j,i in enumerate(a):
        z = "/home/pi/tshark/"+str(j)+".pcap"
        (stdout, stderr) = Popen(['mergecap','-w','/home/pi/tshark/final.pcapng',z], stdout=PIPE).communicate()

for j,i in enumerate(a):
        x = "/home/pi/tshark/"+str(j)+".pcap"
        (stdout, stderr) = Popen(['rm',x], stdout=PIPE).communicate()
