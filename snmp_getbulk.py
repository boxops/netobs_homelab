# Dependencies:
# pip install pysnmplib

# Usage:
# python3 snmp_getbulk.py

import sys
from pysnmp.hlapi import *


iterator = bulkCmd(
    SnmpEngine(),
    CommunityData("homelab"),
    UdpTransportTarget(("192.168.10.200", 161)),
    ContextData(),
    0,
    50,
    ObjectType(ObjectIdentity("1.3.6.1.2.1.2.2.1.2")),
    lexicographicMode=False,
)
for errorIndication, errorStatus, errorIndex, varBinds in iterator:
    if errorIndication or errorStatus:  # SNMP engine or agent errors
        print("Something went wrong")
        sys.exit(1)
    else:
        for varBind in varBinds:  # SNMP response contents
            print(" = ".join([x.prettyPrint() for x in varBind]))
