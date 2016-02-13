#
# PySNMP MIB module FR-MFR-MIB (http://pysnmp.sf.net)
# ASN.1 source http://mibs.snmplabs.com:80/asn1/FR-MFR-MIB
# Produced by pysmi-0.0.7 at Sun Feb 14 00:13:27 2016
# On host bldfarm platform Linux version 4.1.13-100.fc21.x86_64 by user goose
# Using Python version 3.5.0 (default, Jan  5 2016, 17:11:52) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
( InterfaceIndex, ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
( SnmpAdminString, ) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
( ModuleCompliance, NotificationGroup, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
( Bits, Gauge32, Unsigned32, transmission, NotificationType, Counter32, iso, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, MibIdentifier, TimeTicks, Counter64, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "Unsigned32", "transmission", "NotificationType", "Counter32", "iso", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "MibIdentifier", "TimeTicks", "Counter64")
( DisplayString, RowStatus, TextualConvention, TestAndIncr, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TestAndIncr")
mfrMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 47)).setRevisions(("2000-11-30 00:00",))
if mibBuilder.loadTexts: mfrMib.setLastUpdated('200011300000Z')
if mibBuilder.loadTexts: mfrMib.setOrganization('IETF Frame Relay Service MIB (frnetmib)\n                    Working Group')
if mibBuilder.loadTexts: mfrMib.setContactInfo('WG Charter:\n             http://www.ietf.org/html.charters/frnetmib-charter.html\n         WG-email:      frnetmib@sunroof.eng.sun.com\n         Subscribe:     frnetmib-request@sunroof.eng.sun.com\n         Email Archive: ftp://ftp.ietf.org/ietf-mail-archive/frnetmib\n\n         Chair:      Andy Malis\n                     Vivace Networks\n         Email:      Andy.Malis@vivacenetworks.com\n\n         WG editor:  Prayson Pate\n                     Overture Networks\n         Email:      prayson.pate@overturenetworks.com\n\n         Co-author:  Bob Lynch\n                     Overture Networks\n\n         EMail:      bob.lynch@overturenetworks.com\n\n         Co-author:  Kenneth Rehbehn\n                     Megisto Systems, Inc.\n         EMail:      krehbehn@megisto.com')
if mibBuilder.loadTexts: mfrMib.setDescription('This is the MIB used to control and monitor the multilink\n          frame relay (MFR) function described in FRF.16.')
class MfrBundleLinkState(Integer32, TextualConvention):
    subtypeSpec = Integer32.subtypeSpec+ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8,))
    namedValues = NamedValues(("mfrBundleLinkStateAddSent", 1), ("mfrBundleLinkStateAddRx", 2), ("mfrBundleLinkStateAddAckRx", 3), ("mfrBundleLinkStateUp", 4), ("mfrBundleLinkStateIdlePending", 5), ("mfrBundleLinkStateIdle", 6), ("mfrBundleLinkStateDown", 7), ("mfrBundleLinkStateDownIdle", 8),)

mfrMibScalarObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 1))
mfrMibBundleObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 2))
mfrMibBundleLinkObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 3))
mfrMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 4))
mfrMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5))
mfrMibTrapsPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 4, 0))
mfrMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5, 1))
mfrMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 47, 5, 2))
mfrBundleMaxNumBundles = MibScalar((1, 3, 6, 1, 2, 1, 10, 47, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleMaxNumBundles.setDescription('This object is used to inform the manager of the\n          maximum number of bundles supported by this device.')
mfrBundleNextIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 47, 1, 2), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mfrBundleNextIndex.setDescription('This object is used to assist the manager in\n          selecting a value for mfrBundleIndex during row creation\n          in the mfrBundleTable.  It can also be used to avoid race\n          conditions with multiple managers trying to create\n          rows in the table (see RFC 2494 [RFC2494] for one such\n          alogrithm).')
mfrBundleTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 2, 3), )
if mibBuilder.loadTexts: mfrBundleTable.setDescription('The bundle configuration and status table.  There\n          is a one-to-one correspondence between a bundle\n          and an interface represented in the ifTable.\n\n          The following objects of the ifTable have specific\n          meaning for an MFR bundle:\n             ifAdminStatus  - the bundle admin status\n             ifOperStatus   - the bundle operational status\n             ifSpeed        - the current bandwidth of the bundle\n             ifInUcastPkts  - the number of frames received\n                              on the bundle\n             ifOutUcastPkts - the number of frames transmitted\n                              on the bundle\n             ifInErrors     - frame (not fragment) errors\n             ifOutErrors    - frame (not fragment) errors\n             ')
mfrBundleEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1), ).setIndexNames((0, "FR-MFR-MIB", "mfrBundleIndex"))
if mibBuilder.loadTexts: mfrBundleEntry.setDescription('An entry in the bundle table.')
mfrBundleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647)))
if mibBuilder.loadTexts: mfrBundleIndex.setDescription('The index into the table.  While this corresponds\n          to an entry in the ifTable, the value of mfrBundleIndex\n          need not match that of the ifIndex in the ifTable.\n          A manager can use mfrBundleNextIndex to select a unique\n          mfrBundleIndex for creating a new row.')
mfrBundleIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleIfIndex.setDescription('The value must match an entry in the interface\n          table whose ifType must be set to frf16MfrBundle(163).\n\n          For example: if the value of mfrBundleIfIndex is 10,\n          then a corresponding entry should be present in\n\n          the ifTable with an index of 10 and an ifType of 163.')
mfrBundleRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleRowStatus.setDescription('The mfrBundleRowStatus object allows create, change,\n           and delete operations on bundle entries.')
mfrBundleNearEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 4), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleNearEndName.setDescription('The configured name of the bundle.')
mfrBundleFragmentation = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2),)).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleFragmentation.setDescription('Controls whether the bundle performs/accepts\n          fragmentation and re-assembly.  The possible\n          values are:\n\n          enable(1) - Bundle links will fragment frames\n\n          disable(2) - Bundle links will not fragment\n                      frames.')
mfrBundleMaxFragSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1,8184)).clone(-1)).setUnits('Octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleMaxFragSize.setDescription('The maximum fragment size supported.  Note that this\n\n          is only valid if mfrBundleFragmentation is set to enable(1).\n\n          Zero is not a valid fragment size.\n\n          A bundle that does not support fragmentation must return\n          this object with a value of -1.')
mfrBundleTimerHello = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,180)).clone(10)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleTimerHello.setDescription('The configured MFR Hello Timer value.')
mfrBundleTimerAck = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,10)).clone(4)).setUnits('Seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleTimerAck.setDescription('The configured MFR T_ACK value.')
mfrBundleCountMaxRetry = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,5)).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleCountMaxRetry.setDescription('The MFR N_MAX_RETRY value.')
mfrBundleActivationClass = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4,))).clone(namedValues=NamedValues(("mfrBundleActivationClassA", 1), ("mfrBundleActivationClassB", 2), ("mfrBundleActivationClassC", 3), ("mfrBundleActivationClassD", 4),)).clone('mfrBundleActivationClassA')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleActivationClass.setDescription('Controls the conditions under which the bundle is activated.\n          The following settings are available:\n\n             mfrBundleActivationClassA(1) - at least one must link up\n             mfrBundleActivationClassB(2) - all links must be up\n             mfrBundleActivationClassC(3) - a certain number must be\n                                            up.  Refer to\n                                            mfrBundleThreshold for\n                                            the required number.\n             mfrBundleActivationClassD(4) - custom (implementation\n                                            specific).')
mfrBundleThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1,2147483647)).clone(-1)).setUnits('Bundle Links').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleThreshold.setDescription("Specifies the number of links that must be in operational\n          'up' state before the bundle will transition to an\n          operational up/active state.  If the number of\n          operational 'up' links falls below this value,\n          then the bundle will transition to an inactive\n          state.\n\n          Note - this is only valid when mfrBundleActivationClass\n          is set to mfrBundleActivationClassC or, depending upon the\n          implementation, to mfrBundleActivationClassD.  A bundle that\n          is not set to one of these must return this object with a\n          value of -1.")
mfrBundleMaxDiffDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1,2147483647)).clone(-1)).setUnits('Milliseconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleMaxDiffDelay.setDescription('The maximum delay difference between the bundle\n          links.\n\n          A value of -1 indicates that this object does not contain\n          a valid value')
mfrBundleSeqNumSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2,))).clone(namedValues=NamedValues(("seqNumSize12bit", 1), ("seqNumSize24bit", 2),)).clone('seqNumSize12bit')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleSeqNumSize.setDescription('Controls whether the standard FRF.12 12-bit\n          sequence number is used or the optional 24-bit\n          sequence number.')
mfrBundleMaxBundleLinks = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647))).setUnits('Bundle Links').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleMaxBundleLinks.setDescription('The maximum number of bundle links supported for\n          this bundle.')
mfrBundleLinksConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647))).setUnits('Bundle Links').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinksConfigured.setDescription('The number of links configured for the bundle.')
mfrBundleLinksActive = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1,2147483647))).setUnits('Bundle Links').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinksActive.setDescription('The number of links that are active.')
mfrBundleBandwidth = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 17), Integer32()).setUnits('Bits/Sec').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleBandwidth.setDescription('The amount of available bandwidth on the bundle')
mfrBundleFarEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 18), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleFarEndName.setDescription('Name of the bundle received from the far end.')
mfrBundleResequencingErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 3, 1, 19), Counter32()).setUnits('Error Events').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleResequencingErrors.setDescription('A count of the number of resequencing errors.  Each event\n          may correspond to multiple lost frames.  Example:\n          Say sequence number 56, 59 and 60 is received for DLCI 100.\n          It is decided by some means that sequence 57 and 58 is lost.\n          This counter should then be incremented by ONE, even though\n          two frames were lost.')
mfrBundleIfIndexMappingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 2, 4), )
if mibBuilder.loadTexts: mfrBundleIfIndexMappingTable.setDescription('A table mapping the values of ifIndex to the\n           mfrBundleIndex.  This is required in order to find\n           the mfrBundleIndex given an ifIndex.  The mapping of\n           mfrBundleIndex to ifIndex is provided by the\n           mfrBundleIfIndex entry in the mfrBundleTable.')
mfrBundleIfIndexMappingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mfrBundleIfIndexMappingEntry.setDescription('Each row describes one ifIndex to mfrBundleIndex mapping.')
mfrBundleIfIndexMappingIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleIfIndexMappingIndex.setDescription('The mfrBundleIndex of the given ifIndex.')
mfrBundleLinkTable = MibTable((1, 3, 6, 1, 2, 1, 10, 47, 3, 1), )
if mibBuilder.loadTexts: mfrBundleLinkTable.setDescription('The bundle link configuration and status table.  There\n          is a one-to-one correspondence between a bundle link\n          and a physical interface represented in the ifTable.  The\n          ifIndex of the physical interface is used to index the\n          bundle link table, and to create rows.\n\n          The following objects of the ifTable have specific\n          meaning for an MFR bundle link:\n\n             ifAdminStatus  - the bundle link admin status\n             ifOperStatus   - the bundle link operational\n                              status\n\n             ifSpeed        - the bandwidth of the bundle\n                              link interface\n             ifInUcastPkts  - the number of frames received\n                              on the bundle link\n             ifOutUcastPkts - the number of frames transmitted\n                              on the bundle link\n             ifInErrors     - frame and fragment errors\n             ifOutErrors    - frame and fragment errors')
mfrBundleLinkEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mfrBundleLinkEntry.setDescription('An entry in the bundle link table.')
mfrBundleLinkRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleLinkRowStatus.setDescription('The mfrBundleLinkRowStatus object allows create, change,\n          and delete operations on mfrBundleLink entries.\n\n          The create operation must fail if no physical interface\n          is associated with the bundle link.')
mfrBundleLinkConfigBundleIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1,2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleLinkConfigBundleIndex.setDescription('The mfrBundleLinkConfigBundleIndex object allows\n          the manager to control the bundle to which the bundle\n          link is assigned.  If no value were in this field, then\n          the bundle would remain in NOT_READY rowStatus and be\n          unable to go to active.  With an appropriate mfrBundleIndex\n          in this field, then we could put the mfrBundleLink row in\n          NOT_IN_SERVICE or ACTIVE rowStatus.')
mfrBundleLinkNearEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: mfrBundleLinkNearEndName.setDescription('The configured bundle link name that is sent to the far end.')
mfrBundleLinkState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 4), MfrBundleLinkState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkState.setDescription('Current bundle link state as defined by the MFR protocol\n          described in Annex A of FRF.16.')
mfrBundleLinkFarEndName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkFarEndName.setDescription('Name of bundle link received from far end.')
mfrBundleLinkFarEndBundleName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkFarEndBundleName.setDescription('Name of far end bundle for this link received from far end.')
mfrBundleLinkDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1,2147483647))).setUnits('Milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkDelay.setDescription('Current round-trip delay for this bundle link.  The\n          value -1 is returned when an implementation does not\n          support measurement of the bundle link delay.')
mfrBundleLinkFramesControlTx = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 8), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkFramesControlTx.setDescription('Number of MFR control frames sent.')
mfrBundleLinkFramesControlRx = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 9), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkFramesControlRx.setDescription('Number of valid MFR control frames received.')
mfrBundleLinkFramesControlInvalid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 10), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkFramesControlInvalid.setDescription('The number of invalid MFR control frames received.')
mfrBundleLinkTimerExpiredCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 11), Counter32()).setUnits('Timer Expiration Events').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkTimerExpiredCount.setDescription('Number of times the T_HELLO or T_ACK timers expired.')
mfrBundleLinkLoopbackSuspected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 12), Counter32()).setUnits('Loopback Suspected Events').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkLoopbackSuspected.setDescription('The number of times a loopback has been suspected\n          (based upon the use of magic numbers).')
mfrBundleLinkUnexpectedSequence = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 13), Counter32()).setUnits('Frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkUnexpectedSequence.setDescription('The number of data MFR frames discarded because the sequence\n          number of the frame for a DLCI was less than (delayed frame)\n          or equal to (duplicate frame) the one expected for that DLCI.\n\n          Example:\n          Say frames with sequence numbers 56, 58, 59 is received for\n          DLCI 100.  While waiting for sequence number 57 another frame\n          with sequence number 58 arrives.  Frame 58 is discarded and\n          the counter is incremented.')
mfrBundleLinkMismatch = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 47, 3, 1, 1, 14), Counter32()).setUnits('Bundle Name Mismatch Events').setMaxAccess("readonly")
if mibBuilder.loadTexts: mfrBundleLinkMismatch.setDescription('The number of times that the unit has been notified by the\n          remote peer that the bundle name is inconsistent with other\n          bundle links attached to the far-end bundle.')
mfrMibTrapBundleLinkMismatch = NotificationType((1, 3, 6, 1, 2, 1, 10, 47, 4, 0, 1)).setObjects(*(("FR-MFR-MIB", "mfrBundleNearEndName"), ("FR-MFR-MIB", "mfrBundleFarEndName"), ("FR-MFR-MIB", "mfrBundleLinkNearEndName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"),))
if mibBuilder.loadTexts: mfrMibTrapBundleLinkMismatch.setDescription('This trap indicates that a bundle link mismatch has\n          been detected.  The following objects are reported:\n\n          mfrBundleNearEndName:    configured name of near end bundle\n\n          mfrBundleFarEndName:     previously reported name of\n                                far end bundle\n\n          mfrBundleLinkNearEndName: configured name of near end bundle\n\n          mfrBundleLinkFarEndName: reported name of far end bundle\n\n          mfrBundleLinkFarEndBundleName: currently reported name of\n                                far end bundle\n\n          Note: that the configured items may have been configured\n                automatically.\n\n          Note: The mfrBundleLinkMismatch counter is incremented when\n                the trap is sent.')
mfrMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 47, 5, 2, 1)).setObjects(*(("FR-MFR-MIB", "mfrMibBundleGroup"), ("FR-MFR-MIB", "mfrMibBundleLinkGroup"), ("FR-MFR-MIB", "mfrMibTrapGroup"),))
if mibBuilder.loadTexts: mfrMibCompliance.setDescription('The compliance statement for equipment that implements\n          the FRF16 MIB.  All of the current groups are mandatory,\n          but a number of objects may be read-only if the\n          implementation does not allow configuration.')
mfrMibBundleGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 1)).setObjects(*(("FR-MFR-MIB", "mfrBundleMaxNumBundles"), ("FR-MFR-MIB", "mfrBundleNextIndex"), ("FR-MFR-MIB", "mfrBundleIfIndex"), ("FR-MFR-MIB", "mfrBundleRowStatus"), ("FR-MFR-MIB", "mfrBundleNearEndName"), ("FR-MFR-MIB", "mfrBundleFragmentation"), ("FR-MFR-MIB", "mfrBundleMaxFragSize"), ("FR-MFR-MIB", "mfrBundleTimerHello"), ("FR-MFR-MIB", "mfrBundleTimerAck"), ("FR-MFR-MIB", "mfrBundleCountMaxRetry"), ("FR-MFR-MIB", "mfrBundleActivationClass"), ("FR-MFR-MIB", "mfrBundleThreshold"), ("FR-MFR-MIB", "mfrBundleMaxDiffDelay"), ("FR-MFR-MIB", "mfrBundleMaxBundleLinks"), ("FR-MFR-MIB", "mfrBundleLinksConfigured"), ("FR-MFR-MIB", "mfrBundleLinksActive"), ("FR-MFR-MIB", "mfrBundleBandwidth"), ("FR-MFR-MIB", "mfrBundleSeqNumSize"), ("FR-MFR-MIB", "mfrBundleFarEndName"), ("FR-MFR-MIB", "mfrBundleResequencingErrors"), ("FR-MFR-MIB", "mfrBundleIfIndexMappingIndex"),))
if mibBuilder.loadTexts: mfrMibBundleGroup.setDescription('Group of objects describing bundles.')
mfrMibBundleLinkGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 2)).setObjects(*(("FR-MFR-MIB", "mfrBundleLinkRowStatus"), ("FR-MFR-MIB", "mfrBundleLinkConfigBundleIndex"), ("FR-MFR-MIB", "mfrBundleLinkNearEndName"), ("FR-MFR-MIB", "mfrBundleLinkState"), ("FR-MFR-MIB", "mfrBundleLinkFarEndName"), ("FR-MFR-MIB", "mfrBundleLinkFarEndBundleName"), ("FR-MFR-MIB", "mfrBundleLinkDelay"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlTx"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlRx"), ("FR-MFR-MIB", "mfrBundleLinkFramesControlInvalid"), ("FR-MFR-MIB", "mfrBundleLinkTimerExpiredCount"), ("FR-MFR-MIB", "mfrBundleLinkLoopbackSuspected"), ("FR-MFR-MIB", "mfrBundleLinkUnexpectedSequence"), ("FR-MFR-MIB", "mfrBundleLinkMismatch"),))
if mibBuilder.loadTexts: mfrMibBundleLinkGroup.setDescription('Group of objects describing bundle links.')
mfrMibTrapGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 10, 47, 5, 1, 3)).setObjects(*(("FR-MFR-MIB", "mfrMibTrapBundleLinkMismatch"),))
if mibBuilder.loadTexts: mfrMibTrapGroup.setDescription('Group of objects describing notifications (traps).')
mibBuilder.exportSymbols("FR-MFR-MIB", mfrBundleLinkFramesControlInvalid=mfrBundleLinkFramesControlInvalid, mfrBundleMaxNumBundles=mfrBundleMaxNumBundles, mfrBundleTable=mfrBundleTable, mfrBundleActivationClass=mfrBundleActivationClass, MfrBundleLinkState=MfrBundleLinkState, mfrBundleTimerAck=mfrBundleTimerAck, mfrBundleLinksActive=mfrBundleLinksActive, mfrBundleLinkFramesControlTx=mfrBundleLinkFramesControlTx, mfrMibBundleGroup=mfrMibBundleGroup, mfrMibConformance=mfrMibConformance, mfrBundleNextIndex=mfrBundleNextIndex, mfrMibBundleLinkGroup=mfrMibBundleLinkGroup, mfrMibBundleObjects=mfrMibBundleObjects, mfrBundleNearEndName=mfrBundleNearEndName, mfrMibGroups=mfrMibGroups, mfrMib=mfrMib, mfrBundleCountMaxRetry=mfrBundleCountMaxRetry, mfrBundleLinkConfigBundleIndex=mfrBundleLinkConfigBundleIndex, mfrMibBundleLinkObjects=mfrMibBundleLinkObjects, mfrBundleFarEndName=mfrBundleFarEndName, mfrBundleIfIndexMappingIndex=mfrBundleIfIndexMappingIndex, mfrMibCompliances=mfrMibCompliances, mfrBundleLinkTable=mfrBundleLinkTable, mfrBundleLinkNearEndName=mfrBundleLinkNearEndName, mfrBundleTimerHello=mfrBundleTimerHello, mfrBundleLinkTimerExpiredCount=mfrBundleLinkTimerExpiredCount, mfrBundleLinkLoopbackSuspected=mfrBundleLinkLoopbackSuspected, mfrMibCompliance=mfrMibCompliance, mfrBundleEntry=mfrBundleEntry, mfrMibTrapsPrefix=mfrMibTrapsPrefix, mfrBundleBandwidth=mfrBundleBandwidth, mfrBundleLinkMismatch=mfrBundleLinkMismatch, mfrBundleFragmentation=mfrBundleFragmentation, mfrBundleIfIndexMappingTable=mfrBundleIfIndexMappingTable, mfrMibTraps=mfrMibTraps, mfrBundleThreshold=mfrBundleThreshold, mfrBundleLinkEntry=mfrBundleLinkEntry, mfrBundleLinkDelay=mfrBundleLinkDelay, mfrBundleLinkUnexpectedSequence=mfrBundleLinkUnexpectedSequence, mfrBundleMaxFragSize=mfrBundleMaxFragSize, mfrBundleLinkState=mfrBundleLinkState, mfrBundleLinkFarEndName=mfrBundleLinkFarEndName, mfrBundleLinkFarEndBundleName=mfrBundleLinkFarEndBundleName, mfrMibTrapBundleLinkMismatch=mfrMibTrapBundleLinkMismatch, mfrBundleLinkFramesControlRx=mfrBundleLinkFramesControlRx, mfrBundleIfIndex=mfrBundleIfIndex, mfrBundleResequencingErrors=mfrBundleResequencingErrors, mfrBundleIfIndexMappingEntry=mfrBundleIfIndexMappingEntry, mfrMibScalarObjects=mfrMibScalarObjects, mfrBundleMaxBundleLinks=mfrBundleMaxBundleLinks, PYSNMP_MODULE_ID=mfrMib, mfrBundleSeqNumSize=mfrBundleSeqNumSize, mfrBundleRowStatus=mfrBundleRowStatus, mfrBundleLinksConfigured=mfrBundleLinksConfigured, mfrBundleLinkRowStatus=mfrBundleLinkRowStatus, mfrBundleIndex=mfrBundleIndex, mfrMibTrapGroup=mfrMibTrapGroup, mfrBundleMaxDiffDelay=mfrBundleMaxDiffDelay)
