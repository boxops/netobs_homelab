# Dependencies:
# pip install pysnmplib

# Usage:
# python3 snmp_get.py

import sys
from pysnmp.hlapi import *

iterator = getCmd(
    SnmpEngine(),
    CommunityData("homelab"),
    UdpTransportTarget(("192.168.10.200", 161)),
    ContextData(),
    ObjectType(ObjectIdentity("SNMPv2-MIB", "sysDescr", 0)),
    ObjectType(ObjectIdentity("SNMPv2-MIB", "sysUpTime", 0)),
)

errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

if errorIndication or errorStatus:  # SNMP engine or agent errors
    print("Something went wrong")
    sys.exit(1)
else:
    for varBind in varBinds:  # SNMP response contents
        print(" = ".join([x.prettyPrint() for x in varBind]))
