#
# PySNMP MIB module TUNNEL-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/TUNNEL-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:32:19 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( OctetString, Integer, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
( IANAtunnelType, ) = mibBuilder.importSymbols("IANAifType-MIB", "IANAtunnelType")
( ifIndex, InterfaceIndexOrZero, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
( InetAddressType, InetAddress, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
( IPv6FlowLabelOrAny, ) = mibBuilder.importSymbols("IPV6-FLOW-LABEL-MIB", "IPv6FlowLabelOrAny")
( ModuleCompliance, ObjectGroup, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
( Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, iso, MibIdentifier, NotificationType, TimeTicks, transmission, IpAddress, ObjectIdentity, Bits, Counter32, Integer32, ModuleIdentity, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "iso", "MibIdentifier", "NotificationType", "TimeTicks", "transmission", "IpAddress", "ObjectIdentity", "Bits", "Counter32", "Integer32", "ModuleIdentity")
( DisplayString, TextualConvention, RowStatus, StorageType, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
tunnelMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 131)).setRevisions(("2005-05-16 00:00", "1999-08-24 12:00",))
if mibBuilder.loadTexts: tunnelMIB.setLastUpdated('200505160000Z')
if mibBuilder.loadTexts: tunnelMIB.setOrganization('IETF IP Version 6 (IPv6) Working Group')
if mibBuilder.loadTexts: tunnelMIB.setContactInfo(' Dave Thaler\n                 Microsoft Corporation\n                 One Microsoft Way\n                 Redmond, WA  98052-6399\n                 EMail: dthaler@microsoft.com')
if mibBuilder.loadTexts: tunnelMIB.setDescription('The MIB module for management of IP Tunnels,\n               independent of the specific encapsulation scheme in\n               use.\n\n               Copyright (C) The Internet Society (2005).  This\n               version of this MIB module is part of RFC 4087;  see\n               the RFC itself for full legal notices.')
tunnelMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 1))
tunnel = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 1, 1))
tunnelIfTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1), )
if mibBuilder.loadTexts: tunnelIfTable.setDescription('The (conceptual) table containing information on\n               configured tunnels.')
tunnelIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tunnelIfEntry.setDescription('An entry (conceptual row) containing the information\n               on a particular configured tunnel.')
tunnelIfLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfLocalAddress.setDescription('The address of the local endpoint of the tunnel\n               (i.e., the source address used in the outer IP\n               header), or 0.0.0.0 if unknown or if the tunnel is\n               over IPv6.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelIfLocalInetAddress.')
tunnelIfRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfRemoteAddress.setDescription('The address of the remote endpoint of the tunnel\n               (i.e., the destination address used in the outer IP\n               header), or 0.0.0.0 if unknown, or an IPv6 address, or\n               the tunnel is not a point-to-point link (e.g., if it\n               is a 6to4 tunnel).\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelIfRemoteInetAddress.')
tunnelIfEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 3), IANAtunnelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfEncapsMethod.setDescription('The encapsulation method used by the tunnel.')
tunnelIfHopLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfHopLimit.setDescription("The IPv4 TTL or IPv6 Hop Limit to use in the outer IP\n               header.  A value of 0 indicates that the value is\n               copied from the payload's header.")
tunnelIfSecurity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3,))).clone(namedValues=NamedValues(("none", 1), ("ipsec", 2), ("other", 3),))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelIfSecurity.setDescription('The method used by the tunnel to secure the outer IP\n               header.  The value ipsec indicates that IPsec is used\n               between the tunnel endpoints for authentication or\n               encryption or both.  More specific security-related\n               information may be available in a MIB module for the\n               security protocol in use.')
tunnelIfTOS = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2,63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfTOS.setDescription("The method used to set the high 6 bits (the\n               differentiated services codepoint) of the IPv4 TOS or\n               IPv6 Traffic Class in the outer IP header.  A value of\n               -1 indicates that the bits are copied from the\n               payload's header.  A value of -2 indicates that a\n               traffic conditioner is invoked and more information\n               may be available in a traffic conditioner MIB module.\n               A value between 0 and 63 inclusive indicates that the\n               bit field is set to the indicated value.\n\n               Note: instead of the name tunnelIfTOS, a better name\n               would have been tunnelIfDSCPMethod, but the existing\n               name appeared in RFC 2667 and existing objects cannot\n               be renamed.")
tunnelIfFlowLabel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 7), IPv6FlowLabelOrAny()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfFlowLabel.setDescription('The method used to set the IPv6 Flow Label value.\n               This object need not be present in rows where\n               tunnelIfAddressType indicates the tunnel is not over\n               IPv6.  A value of -1 indicates that a traffic\n               conditioner is invoked and more information may be\n               available in a traffic conditioner MIB.  Any other\n               value indicates that the Flow Label field is set to\n               the indicated value.')
tunnelIfAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 8), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfAddressType.setDescription('The type of address in the corresponding\n               tunnelIfLocalInetAddress and tunnelIfRemoteInetAddress\n               objects.')
tunnelIfLocalInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 9), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfLocalInetAddress.setDescription('The address of the local endpoint of the tunnel\n               (i.e., the source address used in the outer IP\n               header).  If the address is unknown, the value is\n               0.0.0.0 for IPv4 or :: for IPv6.  The type of this\n               object is given by tunnelIfAddressType.')
tunnelIfRemoteInetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 10), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfRemoteInetAddress.setDescription('The address of the remote endpoint of the tunnel\n               (i.e., the destination address used in the outer IP\n               header).  If the address is unknown or the tunnel is\n               not a point-to-point link (e.g., if it is a 6to4\n               tunnel), the value is 0.0.0.0 for tunnels over IPv4 or\n               :: for tunnels over IPv6.  The type of this object is\n               given by tunnelIfAddressType.')
tunnelIfEncapsLimit = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255),))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tunnelIfEncapsLimit.setDescription('The maximum number of additional encapsulations\n               permitted for packets undergoing encapsulation at this\n               node.  A value of -1 indicates that no limit is\n               present (except as a result of the packet size).')
tunnelConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2), )
if mibBuilder.loadTexts: tunnelConfigTable.setDescription('The (conceptual) table containing information on\n               configured tunnels.  This table can be used to map a\n               set of tunnel endpoints to the associated ifIndex\n               value.  It can also be used for row creation.  Note\n               that every row in the tunnelIfTable with a fixed IPv4\n               destination address should have a corresponding row in\n               the tunnelConfigTable, regardless of whether it was\n               created via SNMP.\n\n               Since this table does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigTable.')
tunnelConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1), ).setIndexNames((0, "TUNNEL-MIB", "tunnelConfigLocalAddress"), (0, "TUNNEL-MIB", "tunnelConfigRemoteAddress"), (0, "TUNNEL-MIB", "tunnelConfigEncapsMethod"), (0, "TUNNEL-MIB", "tunnelConfigID"))
if mibBuilder.loadTexts: tunnelConfigEntry.setDescription('An entry (conceptual row) containing the information\n               on a particular configured tunnel.\n\n               Since this entry does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigEntry.')
tunnelConfigLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: tunnelConfigLocalAddress.setDescription('The address of the local endpoint of the tunnel, or\n               0.0.0.0 if the device is free to choose any of its\n               addresses at tunnel establishment time.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigLocalAddress.')
tunnelConfigRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 2), IpAddress())
if mibBuilder.loadTexts: tunnelConfigRemoteAddress.setDescription('The address of the remote endpoint of the tunnel.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigRemoteAddress.')
tunnelConfigEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 3), IANAtunnelType())
if mibBuilder.loadTexts: tunnelConfigEncapsMethod.setDescription('The encapsulation method used by the tunnel.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigEncapsMethod.')
tunnelConfigID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: tunnelConfigID.setDescription('An identifier used to distinguish between multiple\n               tunnels of the same encapsulation method, with the\n               same endpoints.  If the encapsulation protocol only\n               allows one tunnel per set of endpoint addresses (such\n               as for GRE or IP-in-IP), the value of this object is\n               1.  For encapsulation methods (such as L2F) which\n               allow multiple parallel tunnels, the manager is\n               responsible for choosing any ID which does not\n               conflict with an existing row, such as choosing a\n               random number.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigID.')
tunnelConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelConfigIfIndex.setDescription('If the value of tunnelConfigStatus for this row is\n               active, then this object contains the value of ifIndex\n               corresponding to the tunnel interface.  A value of 0\n               is not legal in the active state, and means that the\n               interface index has not yet been assigned.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigIfIndex.')
tunnelConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelConfigStatus.setDescription('The status of this row, by which new entries may be\n               created, or old entries deleted from this table.  The\n               agent need not support setting this object to\n               createAndWait or notInService since there are no other\n               writable objects in this table, and writable objects\n               in rows of corresponding tables such as the\n               tunnelIfTable may be modified while this row is\n               active.\n\n               To create a row in this table for an encapsulation\n               method which does not support multiple parallel\n               tunnels with the same endpoints, the management\n               station should simply use a tunnelConfigID of 1, and\n               set tunnelConfigStatus to createAndGo.  For\n               encapsulation methods such as L2F which allow multiple\n               parallel tunnels, the management station may select a\n               pseudo-random number to use as the tunnelConfigID and\n               set tunnelConfigStatus to createAndGo.  In the event\n               that this ID is already in use and an\n               inconsistentValue is returned in response to the set\n               operation, the management station should simply select\n               a new pseudo-random number and retry the operation.\n\n               Creating a row in this table will cause an interface\n               index to be assigned by the agent in an\n               implementation-dependent manner, and corresponding\n               rows will be instantiated in the ifTable and the\n               tunnelIfTable.  The status of this row will become\n               active as soon as the agent assigns the interface\n               index, regardless of whether the interface is\n               operationally up.\n\n               Deleting a row in this table will likewise delete the\n               corresponding row in the ifTable and in the\n               tunnelIfTable.\n\n               Since this object does not support IPv6, it is\n               deprecated in favor of tunnelInetConfigStatus.')
tunnelInetConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3), )
if mibBuilder.loadTexts: tunnelInetConfigTable.setDescription('The (conceptual) table containing information on\n               configured tunnels.  This table can be used to map a\n               set of tunnel endpoints to the associated ifIndex\n               value.  It can also be used for row creation.  Note\n               that every row in the tunnelIfTable with a fixed\n               destination address should have a corresponding row in\n               the tunnelInetConfigTable, regardless of whether it\n               was created via SNMP.')
tunnelInetConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1), ).setIndexNames((0, "TUNNEL-MIB", "tunnelInetConfigAddressType"), (0, "TUNNEL-MIB", "tunnelInetConfigLocalAddress"), (0, "TUNNEL-MIB", "tunnelInetConfigRemoteAddress"), (0, "TUNNEL-MIB", "tunnelInetConfigEncapsMethod"), (0, "TUNNEL-MIB", "tunnelInetConfigID"))
if mibBuilder.loadTexts: tunnelInetConfigEntry.setDescription('An entry (conceptual row) containing the information\n               on a particular configured tunnel.  Note that there is\n               a 128 subid maximum for object OIDs.  Implementers\n               need to be aware that if the total number of octets in\n               tunnelInetConfigLocalAddress and\n               tunnelInetConfigRemoteAddress exceeds 110 then OIDs of\n               column instances in this table will have more than 128\n               sub-identifiers and cannot be accessed using SNMPv1,\n               SNMPv2c, or SNMPv3.  In practice this is not expected\n               to be a problem since IPv4 and IPv6 addresses will not\n               cause the limit to be reached, but if other types are\n               supported by an agent, care must be taken to ensure\n               that the sum of the lengths do not cause the limit to\n               be exceeded.')
tunnelInetConfigAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tunnelInetConfigAddressType.setDescription('The address type over which the tunnel encapsulates\n               packets.')
tunnelInetConfigLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 2), InetAddress())
if mibBuilder.loadTexts: tunnelInetConfigLocalAddress.setDescription('The address of the local endpoint of the tunnel, or\n               0.0.0.0 (for IPv4) or :: (for IPv6) if the device is\n               free to choose any of its addresses at tunnel\n               establishment time.')
tunnelInetConfigRemoteAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 3), InetAddress())
if mibBuilder.loadTexts: tunnelInetConfigRemoteAddress.setDescription('The address of the remote endpoint of the tunnel.')
tunnelInetConfigEncapsMethod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 4), IANAtunnelType())
if mibBuilder.loadTexts: tunnelInetConfigEncapsMethod.setDescription('The encapsulation method used by the tunnel.')
tunnelInetConfigID = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: tunnelInetConfigID.setDescription('An identifier used to distinguish between multiple\n               tunnels of the same encapsulation method, with the\n               same endpoints.  If the encapsulation protocol only\n               allows one tunnel per set of endpoint addresses (such\n               as for GRE or IP-in-IP), the value of this object is\n               1.  For encapsulation methods (such as L2F) which\n               allow multiple parallel tunnels, the manager is\n               responsible for choosing any ID which does not\n               conflict with an existing row, such as choosing a\n               random number.')
tunnelInetConfigIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tunnelInetConfigIfIndex.setDescription('If the value of tunnelInetConfigStatus for this row\n               is active, then this object contains the value of\n               ifIndex corresponding to the tunnel interface.  A\n               value of 0 is not legal in the active state, and means\n               that the interface index has not yet been assigned.')
tunnelInetConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelInetConfigStatus.setDescription('The status of this row, by which new entries may be\n               created, or old entries deleted from this table.  The\n               agent need not support setting this object to\n               createAndWait or notInService since there are no other\n               writable objects in this table, and writable objects\n               in rows of corresponding tables such as the\n               tunnelIfTable may be modified while this row is\n               active.\n\n               To create a row in this table for an encapsulation\n               method which does not support multiple parallel\n               tunnels with the same endpoints, the management\n               station should simply use a tunnelInetConfigID of 1,\n               and set tunnelInetConfigStatus to createAndGo.  For\n               encapsulation methods such as L2F which allow multiple\n               parallel tunnels, the management station may select a\n               pseudo-random number to use as the tunnelInetConfigID\n               and set tunnelInetConfigStatus to createAndGo.  In the\n               event that this ID is already in use and an\n               inconsistentValue is returned in response to the set\n               operation, the management station should simply select\n               a new pseudo-random number and retry the operation.\n\n               Creating a row in this table will cause an interface\n               index to be assigned by the agent in an\n               implementation-dependent manner, and corresponding\n               rows will be instantiated in the ifTable and the\n               tunnelIfTable.  The status of this row will become\n               active as soon as the agent assigns the interface\n               index, regardless of whether the interface is\n               operationally up.\n\n               Deleting a row in this table will likewise delete the\n               corresponding row in the ifTable and in the\n               tunnelIfTable.')
tunnelInetConfigStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 131, 1, 1, 3, 1, 8), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tunnelInetConfigStorageType.setDescription('The storage type of this row.  If the row is\n               permanent(4), no objects in the row need be writable.')
tunnelMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2))
tunnelMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2, 1))
tunnelMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 131, 2, 2))
tunnelMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 1)).setObjects(*(("TUNNEL-MIB", "tunnelMIBBasicGroup"),))
if mibBuilder.loadTexts: tunnelMIBCompliance.setDescription('The (deprecated) IPv4-only compliance statement for\n               the IP Tunnel MIB.\n\n               This is deprecated in favor of\n               tunnelMIBInetFullCompliance and\n               tunnelMIBInetReadOnlyCompliance.')
tunnelMIBInetFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 2)).setObjects(*(("TUNNEL-MIB", "tunnelMIBInetGroup"),))
if mibBuilder.loadTexts: tunnelMIBInetFullCompliance.setDescription('The full compliance statement for the IP Tunnel MIB.')
tunnelMIBInetReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 131, 2, 1, 3)).setObjects(*(("TUNNEL-MIB", "tunnelMIBInetGroup"),))
if mibBuilder.loadTexts: tunnelMIBInetReadOnlyCompliance.setDescription('The read-only compliance statement for the IP Tunnel\n               MIB.')
tunnelMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 1)).setObjects(*(("TUNNEL-MIB", "tunnelIfLocalAddress"), ("TUNNEL-MIB", "tunnelIfRemoteAddress"), ("TUNNEL-MIB", "tunnelIfEncapsMethod"), ("TUNNEL-MIB", "tunnelIfHopLimit"), ("TUNNEL-MIB", "tunnelIfTOS"), ("TUNNEL-MIB", "tunnelIfSecurity"), ("TUNNEL-MIB", "tunnelConfigIfIndex"), ("TUNNEL-MIB", "tunnelConfigStatus"),))
if mibBuilder.loadTexts: tunnelMIBBasicGroup.setDescription('A collection of objects to support basic management\n               of IPv4 Tunnels.  Since this group cannot support\n               IPv6, it is deprecated in favor of\n               tunnelMIBInetGroup.')
tunnelMIBInetGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 131, 2, 2, 2)).setObjects(*(("TUNNEL-MIB", "tunnelIfAddressType"), ("TUNNEL-MIB", "tunnelIfLocalInetAddress"), ("TUNNEL-MIB", "tunnelIfRemoteInetAddress"), ("TUNNEL-MIB", "tunnelIfEncapsMethod"), ("TUNNEL-MIB", "tunnelIfEncapsLimit"), ("TUNNEL-MIB", "tunnelIfHopLimit"), ("TUNNEL-MIB", "tunnelIfTOS"), ("TUNNEL-MIB", "tunnelIfFlowLabel"), ("TUNNEL-MIB", "tunnelIfSecurity"), ("TUNNEL-MIB", "tunnelInetConfigIfIndex"), ("TUNNEL-MIB", "tunnelInetConfigStatus"), ("TUNNEL-MIB", "tunnelInetConfigStorageType"),))
if mibBuilder.loadTexts: tunnelMIBInetGroup.setDescription('A collection of objects to support basic management\n               of IPv4 and IPv6 Tunnels.')
mibBuilder.exportSymbols("TUNNEL-MIB", tunnel=tunnel, tunnelIfAddressType=tunnelIfAddressType, tunnelInetConfigID=tunnelInetConfigID, tunnelMIBObjects=tunnelMIBObjects, tunnelInetConfigEncapsMethod=tunnelInetConfigEncapsMethod, tunnelMIBInetReadOnlyCompliance=tunnelMIBInetReadOnlyCompliance, tunnelIfTable=tunnelIfTable, tunnelMIBConformance=tunnelMIBConformance, tunnelIfSecurity=tunnelIfSecurity, tunnelInetConfigEntry=tunnelInetConfigEntry, tunnelIfTOS=tunnelIfTOS, PYSNMP_MODULE_ID=tunnelMIB, tunnelIfEntry=tunnelIfEntry, tunnelConfigEncapsMethod=tunnelConfigEncapsMethod, tunnelInetConfigStatus=tunnelInetConfigStatus, tunnelIfRemoteInetAddress=tunnelIfRemoteInetAddress, tunnelMIB=tunnelMIB, tunnelMIBGroups=tunnelMIBGroups, tunnelConfigRemoteAddress=tunnelConfigRemoteAddress, tunnelConfigTable=tunnelConfigTable, tunnelInetConfigRemoteAddress=tunnelInetConfigRemoteAddress, tunnelConfigEntry=tunnelConfigEntry, tunnelConfigStatus=tunnelConfigStatus, tunnelConfigID=tunnelConfigID, tunnelIfRemoteAddress=tunnelIfRemoteAddress, tunnelMIBBasicGroup=tunnelMIBBasicGroup, tunnelIfLocalInetAddress=tunnelIfLocalInetAddress, tunnelIfFlowLabel=tunnelIfFlowLabel, tunnelInetConfigAddressType=tunnelInetConfigAddressType, tunnelMIBCompliance=tunnelMIBCompliance, tunnelIfLocalAddress=tunnelIfLocalAddress, tunnelInetConfigIfIndex=tunnelInetConfigIfIndex, tunnelIfEncapsMethod=tunnelIfEncapsMethod, tunnelConfigIfIndex=tunnelConfigIfIndex, tunnelInetConfigStorageType=tunnelInetConfigStorageType, tunnelMIBInetFullCompliance=tunnelMIBInetFullCompliance, tunnelIfHopLimit=tunnelIfHopLimit, tunnelMIBInetGroup=tunnelMIBInetGroup, tunnelInetConfigTable=tunnelInetConfigTable, tunnelConfigLocalAddress=tunnelConfigLocalAddress, tunnelIfEncapsLimit=tunnelIfEncapsLimit, tunnelMIBCompliances=tunnelMIBCompliances, tunnelInetConfigLocalAddress=tunnelInetConfigLocalAddress)
