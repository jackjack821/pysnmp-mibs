# PySNMP SMI module. Autogenerated from smidump -f python INET-ADDRESS-MIB
# by libsmi2pysnmp-0.0.3-alpha at Wed Nov 10 12:10:21 2004,
# Python version (2, 2, 1, 'final', 0)

# Imported just in case new ASN.1 types would be created
from pysnmp.asn1 import subtypes

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "mib-2")
( TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention")

# Types

class InetAddress(OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 255), )
    pass

class InetAddressDNS(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(1, 255), )
    pass

class InetAddressIPv4(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(4, 4), )
    pass

class InetAddressIPv4z(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(8, 8), )
    pass

class InetAddressIPv6(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(16, 16), )
    pass

class InetAddressIPv6z(TextualConvention, OctetString):
    subtypeConstraints = OctetString.subtypeConstraints + ( subtypes.ValueRangeConstraint(20, 20), )
    pass

class InetAddressPrefixLength(Unsigned32):
    pass

class InetAddressType(Integer):
    subtypeConstraints = Integer.subtypeConstraints + ( subtypes.SingleValueConstraint(16,1,4,2,0,3,), )
    namedValues = Integer.namedValues.clone(("unknown", 0), ("ipv4", 1), ("dns", 16), ("ipv6", 2), ("ipv4z", 3), ("ipv6z", 4), )
    pass

class InetAutonomousSystemNumber(Unsigned32):
    pass

class InetPortNumber(Unsigned32):
    subtypeConstraints = Unsigned32.subtypeConstraints + ( subtypes.ValueRangeConstraint(0, 65535), )
    pass


# Objects

inetAddressMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 76))

# Augmentions

# Exports

# Types
mibBuilder.exportSymbols("INET-ADDRESS-MIB", InetAddress=InetAddress, InetAddressDNS=InetAddressDNS, InetAddressIPv4=InetAddressIPv4, InetAddressIPv4z=InetAddressIPv4z, InetAddressIPv6=InetAddressIPv6, InetAddressIPv6z=InetAddressIPv6z, InetAddressPrefixLength=InetAddressPrefixLength, InetAddressType=InetAddressType, InetAutonomousSystemNumber=InetAutonomousSystemNumber, InetPortNumber=InetPortNumber)

# Objects
mibBuilder.exportSymbols("INET-ADDRESS-MIB", inetAddressMIB=inetAddressMIB)
