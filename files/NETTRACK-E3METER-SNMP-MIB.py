#
# PySNMP MIB module NETTRACK-E3METER-SNMP-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/e3meter-ipm.mib
# Produced by pysmi-0.0.7 at Fri Jun  3 10:56:07 2016
# On host luna platform Linux version 4.5.2-1-custom by user maxf
# Using Python version 3.5.1 (default, Mar  3 2016, 09:29:07) 
#
( Integer, OctetString, ObjectIdentifier, ) = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
( ModuleCompliance, NotificationGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
( MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, enterprises, iso, ModuleIdentity, Bits, Counter32, Unsigned32, ObjectIdentity, TimeTicks, Gauge32, NotificationType, Integer32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "enterprises", "iso", "ModuleIdentity", "Bits", "Counter32", "Unsigned32", "ObjectIdentity", "TimeTicks", "Gauge32", "NotificationType", "Integer32")
( TextualConvention, DisplayString, ) = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nettrack = MibIdentifier((1, 3, 6, 1, 4, 1, 21695))
public = MibIdentifier((1, 3, 6, 1, 4, 1, 21695, 1))
e3Mib = ModuleIdentity((1, 3, 6, 1, 4, 1, 21695, 1, 10)).setRevisions(("2012-04-12 00:00", "2011-11-02 00:00", "2011-08-19 00:00", "2011-01-26 00:00", "2010-12-06 00:00", "2010-10-20 00:00",))
e3Ipm = MibIdentifier((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7))
class Watts(Integer32, TextualConvention):
    pass

class VoltAmpereReactives(Integer32, TextualConvention):
    pass

class VoltAmperes(Integer32, TextualConvention):
    pass

class WattHours(Integer32, TextualConvention):
    pass

class VoltAmpereReactiveHours(Integer32, TextualConvention):
    pass

class VoltAmpereHours(Integer32, TextualConvention):
    pass

class MilliAmperes(Integer32, TextualConvention):
    pass

class MilliVolts(Integer32, TextualConvention):
    pass

class MilliHertz(Integer32, TextualConvention):
    pass

class DeciDegreesCelsius(Integer32, TextualConvention):
    pass

class Permil(Integer32, TextualConvention):
    pass

e3IpmInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1))
e3IpmInfoSerial = MibScalar((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 1), Integer32()).setMaxAccess("readonly")
e3IpmInfoModel = MibScalar((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 2), Integer32()).setMaxAccess("readonly")
e3IpmInfoHWVersion = MibScalar((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1,))).clone(namedValues=NamedValues(("rev-a", 0), ("rev-b", 1),))).setMaxAccess("readonly")
e3IpmInfoFWVersion = MibScalar((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 4), Integer32()).setMaxAccess("readonly")
e3IpmInfoMeters = MibScalar((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 1, 5), Integer32()).setMaxAccess("readonly")
e3IpmMeterTable = MibTable((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2), )
e3IpmMeterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1), ).setIndexNames((0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmMeter"))
e3IpmMeter = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 1), Integer32()).setMaxAccess("readonly")
e3IpmEnergyP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 2), WattHours()).setUnits('Wh').setMaxAccess("readonly")
e3IpmEnergyQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 3), VoltAmpereReactiveHours()).setUnits('varh').setMaxAccess("readonly")
e3IpmEnergyS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 4), VoltAmpereHours()).setUnits('VAh').setMaxAccess("readonly")
e3IpmPowerP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 5), Watts()).setUnits('W').setMaxAccess("readonly")
e3IpmPowerQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 6), VoltAmpereReactives()).setUnits('var').setMaxAccess("readonly")
e3IpmPowerS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 7), VoltAmperes()).setUnits('VA').setMaxAccess("readonly")
e3IpmUrms = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 8), MilliVolts()).setUnits('mV').setMaxAccess("readonly")
e3IpmIrms = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 9), MilliAmperes()).setUnits('mA').setMaxAccess("readonly")
e3IpmFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 10), MilliHertz()).setUnits('mHz').setMaxAccess("readonly")
e3IpmChannelName = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,15))).setMaxAccess("readonly")
e3IpmChannelType = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1,))).clone(namedValues=NamedValues(("live-wire", 0), ("neutral-wire", 1),))).setMaxAccess("readonly")
e3IpmSensorTable = MibTable((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3), )
e3IpmSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1), ).setIndexNames((0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmSensor"))
e3IpmSensor = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 1), Integer32()).setMaxAccess("readonly")
e3IpmSensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2,))).clone(namedValues=NamedValues(("none", 0), ("temp", 1), ("temp-humidity", 2),))).setMaxAccess("readonly")
e3IpmSensorVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,15))).setMaxAccess("readonly")
e3IpmSensorTemperatureCelsius = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 4), DeciDegreesCelsius()).setUnits('deg-C/10').setMaxAccess("readonly")
e3IpmSensorHumidity = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 3, 1, 5), Permil()).setUnits('/1000').setMaxAccess("readonly")
e3IpmPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4), )
e3IpmPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1), ).setIndexNames((0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmPGroup"))
e3IpmPGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 1), Integer32()).setMaxAccess("readonly")
e3IpmPGName = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,15))).setMaxAccess("readonly")
e3IpmPGMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 3), Integer32()).setMaxAccess("readonly")
e3IpmPGEnergyP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 4), WattHours()).setUnits('Wh').setMaxAccess("readonly")
e3IpmPGEnergyQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 5), VoltAmpereReactiveHours()).setUnits('varh').setMaxAccess("readonly")
e3IpmPGEnergyS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 6), VoltAmpereHours()).setUnits('VAh').setMaxAccess("readonly")
e3IpmPGPowerP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 7), Watts()).setUnits('W').setMaxAccess("readonly")
e3IpmPGPowerQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 8), VoltAmpereReactives()).setUnits('var').setMaxAccess("readonly")
e3IpmPGPowerS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 9), VoltAmperes()).setUnits('VA').setMaxAccess("readonly")
e3IpmPGIrms = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 4, 1, 10), MilliAmperes()).setUnits('mA').setMaxAccess("readonly")
e3IpmUGroupTable = MibTable((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5), )
e3IpmUGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1), ).setIndexNames((0, "NETTRACK-E3METER-SNMP-MIB", "e3IpmUGroup"))
e3IpmUGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 1), Integer32()).setMaxAccess("readonly")
e3IpmUGName = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0,15))).setMaxAccess("readonly")
e3IpmUGMembers = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 3), Integer32()).setMaxAccess("readonly")
e3IpmUGEnergyP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 4), WattHours()).setUnits('Wh').setMaxAccess("readonly")
e3IpmUGEnergyQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 5), VoltAmpereReactiveHours()).setUnits('varh').setMaxAccess("readonly")
e3IpmUGEnergyS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 6), VoltAmpereHours()).setUnits('VAh').setMaxAccess("readonly")
e3IpmUGPowerP = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 7), Watts()).setUnits('W').setMaxAccess("readonly")
e3IpmUGPowerQ = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 8), VoltAmpereReactives()).setUnits('var').setMaxAccess("readonly")
e3IpmUGPowerS = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 9), VoltAmperes()).setUnits('VA').setMaxAccess("readonly")
e3IpmUGIrms = MibTableColumn((1, 3, 6, 1, 4, 1, 21695, 1, 10, 7, 5, 1, 10), MilliAmperes()).setUnits('mA').setMaxAccess("readonly")
mibBuilder.exportSymbols("NETTRACK-E3METER-SNMP-MIB", e3IpmUGPowerP=e3IpmUGPowerP, WattHours=WattHours, e3IpmUGroupTable=e3IpmUGroupTable, MilliHertz=MilliHertz, e3IpmUGEnergyQ=e3IpmUGEnergyQ, e3IpmPGPowerQ=e3IpmPGPowerQ, e3IpmInfoFWVersion=e3IpmInfoFWVersion, e3IpmSensorTable=e3IpmSensorTable, e3Ipm=e3Ipm, e3IpmInfoMeters=e3IpmInfoMeters, e3IpmPGMembers=e3IpmPGMembers, MilliVolts=MilliVolts, e3IpmMeterEntry=e3IpmMeterEntry, e3IpmPowerQ=e3IpmPowerQ, e3IpmPGPowerP=e3IpmPGPowerP, DeciDegreesCelsius=DeciDegreesCelsius, e3IpmInfoModel=e3IpmInfoModel, e3IpmPowerS=e3IpmPowerS, e3IpmPowerP=e3IpmPowerP, e3IpmMeter=e3IpmMeter, VoltAmperes=VoltAmperes, e3IpmPGroupEntry=e3IpmPGroupEntry, e3IpmPGEnergyS=e3IpmPGEnergyS, e3IpmUGPowerQ=e3IpmUGPowerQ, e3IpmPGroupTable=e3IpmPGroupTable, e3IpmPGPowerS=e3IpmPGPowerS, e3IpmUGMembers=e3IpmUGMembers, e3IpmUGName=e3IpmUGName, e3Mib=e3Mib, e3IpmSensorTemperatureCelsius=e3IpmSensorTemperatureCelsius, nettrack=nettrack, PYSNMP_MODULE_ID=e3Mib, Permil=Permil, public=public, e3IpmPGroup=e3IpmPGroup, VoltAmpereReactiveHours=VoltAmpereReactiveHours, e3IpmUGroupEntry=e3IpmUGroupEntry, e3IpmSensorHumidity=e3IpmSensorHumidity, e3IpmUGIrms=e3IpmUGIrms, e3IpmInfoHWVersion=e3IpmInfoHWVersion, e3IpmEnergyQ=e3IpmEnergyQ, e3IpmChannelName=e3IpmChannelName, VoltAmpereReactives=VoltAmpereReactives, e3IpmInfoSerial=e3IpmInfoSerial, e3IpmEnergyS=e3IpmEnergyS, e3IpmEnergyP=e3IpmEnergyP, e3IpmUGroup=e3IpmUGroup, MilliAmperes=MilliAmperes, e3IpmUGEnergyS=e3IpmUGEnergyS, e3IpmChannelType=e3IpmChannelType, e3IpmSensor=e3IpmSensor, e3IpmFrequency=e3IpmFrequency, e3IpmUrms=e3IpmUrms, e3IpmSensorType=e3IpmSensorType, e3IpmPGEnergyQ=e3IpmPGEnergyQ, Watts=Watts, e3IpmPGEnergyP=e3IpmPGEnergyP, e3IpmUGEnergyP=e3IpmUGEnergyP, e3IpmPGName=e3IpmPGName, e3IpmInfo=e3IpmInfo, e3IpmUGPowerS=e3IpmUGPowerS, e3IpmSensorEntry=e3IpmSensorEntry, e3IpmSensorVersion=e3IpmSensorVersion, e3IpmPGIrms=e3IpmPGIrms, e3IpmIrms=e3IpmIrms, VoltAmpereHours=VoltAmpereHours, e3IpmMeterTable=e3IpmMeterTable)
