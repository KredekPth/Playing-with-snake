import argparse
from pysnmp.entity.rfc3413.oneliner import cmdgen
parser = argparse.ArgumentParser(description='Use optional arguments to add your own host address, port number and SNMP tag \n Exampe Usage for this script: python script.py -H 192.168.0.1 -P 161 -T public')




parser.add_argument('-H', '--Host', help="IP address of your object you want to check", required=True)
parser.add_argument('-P', '--Port', help="Port number of your object you want to check", required=True)
parser.add_argument('-T', '--Tag', help="SNMP tag of your object you want to check, default is 'public' ", required=True)

args = parser.parse_args()

print("Values : ", str(args.Host),int(args.Port),str(args.Tag))



SNMP_HOST = str(args.Host)
SNMP_PORT = int(args.Port)
SNMP_COMMUNITY = str(args.Tag)

NAMES = ["Free-Disk-space","Cpu-Temp", "System-Temp", "Free-RAM"]

cmdGen = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
    cmdgen.CommunityData(SNMP_COMMUNITY),
    cmdgen.UdpTransportTarget((SNMP_HOST,SNMP_PORT)),
    '1.3.6.1.4.1.24681.1.2.17.1.5.1',  #Free space
    '.1.3.6.1.4.1.24681.1.2.5.0',      #CPU Temperature
    '1.3.6.1.4.1.24681.1.2.6.0',       #System Temperature
    '1.3.6.1.4.1.24681.1.2.3.0'        #Free RAM
)
i = 0
for i in range(0,len(NAMES),1):

    print('%s = %s \n' % (NAMES[i],varBinds.__getitem__(i)[1]))
    i=+1



