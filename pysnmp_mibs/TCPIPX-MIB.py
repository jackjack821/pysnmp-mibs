# PySNMP SMI module. Autogenerated from smidump -f python TCPIPX-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:37 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( MibVariable, MibTable, MibTableRow, MibTableColumn, ) = mibBuilder.importSymbols("RFC-1212", "MibVariable", "MibTable", "MibTableRow", "MibTableColumn")
( enterprises, ) = mibBuilder.importSymbols("RFC1155-SMI", "enterprises")
( Bits, Integer32, MibIdentifier, TimeTicks, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "MibIdentifier", "TimeTicks")

# Types

class IpxAddress(OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(10, 10), )
    pass


# Objects

novell = MibIdentifier((1, 3, 6, 1, 4, 1, 23))
mibDoc = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2))
tcpx = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29))
tcpxTcp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 1))
tcpIpxConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1))
tcpIpxConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1)).setIndexNames((0, "TCPIPX-MIB", "tcpIpxConnLocalAddress"), (0, "TCPIPX-MIB", "tcpIpxConnLocalPort"), (0, "TCPIPX-MIB", "tcpIpxConnRemAddress"), (0, "TCPIPX-MIB", "tcpIpxConnRemPort"))
tcpIpxConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 1)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(4,5,7,11,6,9,8,12,1,10,3,2,)).addNamedValues(("closed", 1), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), )).setMaxAccess("readwrite"))
tcpIpxConnLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 2)).setColumnInitializer(MibVariable((), IpxAddress()).setMaxAccess("readonly"))
tcpIpxConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 3)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
tcpIpxConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 4)).setColumnInitializer(MibVariable((), IpxAddress()).setMaxAccess("readonly"))
tcpIpxConnRemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 1, 1, 5)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
tcpUnspecConnTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2))
tcpUnspecConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1)).setIndexNames((0, "TCPIPX-MIB", "tcpUnspecConnLocalPort"))
tcpUnspecConnState = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer().addConstraints(subtypes.SingleValueConstraint(12,2,1,)).addNamedValues(("closed", 1), ("deleteTCB", 12), ("listen", 2), )).setMaxAccess("readwrite"))
tcpUnspecConnLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 1, 2, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
tcpxUdp = MibIdentifier((1, 3, 6, 1, 4, 1, 23, 2, 29, 2))
udpIpxTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1))
udpIpxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1)).setIndexNames((0, "TCPIPX-MIB", "udpIpxLocalAddress"), (0, "TCPIPX-MIB", "udpIpxLocalPort"))
udpIpxLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 1)).setColumnInitializer(MibVariable((), IpxAddress()).setMaxAccess("readonly"))
udpIpxLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 1, 1, 2)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))
udpUnspecTable = MibTable((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2))
udpUnspecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1)).setIndexNames((0, "TCPIPX-MIB", "udpUnspecLocalPort"))
udpUnspecLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 23, 2, 29, 2, 2, 1, 1)).setColumnInitializer(MibVariable((), Integer32().addConstraints(subtypes.ValueRangeConstraint(0, 65535))).setMaxAccess("readonly"))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("TCPIPX-MIB", IpxAddress=IpxAddress)

# Objects
mibBuilder.exportSymbols("TCPIPX-MIB", novell=novell, mibDoc=mibDoc, tcpx=tcpx, tcpxTcp=tcpxTcp, tcpIpxConnTable=tcpIpxConnTable, tcpIpxConnEntry=tcpIpxConnEntry, tcpIpxConnState=tcpIpxConnState, tcpIpxConnLocalAddress=tcpIpxConnLocalAddress, tcpIpxConnLocalPort=tcpIpxConnLocalPort, tcpIpxConnRemAddress=tcpIpxConnRemAddress, tcpIpxConnRemPort=tcpIpxConnRemPort, tcpUnspecConnTable=tcpUnspecConnTable, tcpUnspecConnEntry=tcpUnspecConnEntry, tcpUnspecConnState=tcpUnspecConnState, tcpUnspecConnLocalPort=tcpUnspecConnLocalPort, tcpxUdp=tcpxUdp, udpIpxTable=udpIpxTable, udpIpxEntry=udpIpxEntry, udpIpxLocalAddress=udpIpxLocalAddress, udpIpxLocalPort=udpIpxLocalPort, udpUnspecTable=udpUnspecTable, udpUnspecEntry=udpUnspecEntry, udpUnspecLocalPort=udpUnspecLocalPort)
