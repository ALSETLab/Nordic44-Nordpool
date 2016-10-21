'''
Created on 2015-02-24
author: trabuzin at gmail dot com
'''

from nordic44.readraw import Reader
from nordic44.torecord import Record

reader = Reader(Raw2Record.settings.globalworkdir, r'X:/dev/N44_WP7/N44 Snapshots/N44_20150401/h0_after_PF.raw')

lista = reader.get_list_of_raw_files()
reader.open_raw(lista[0])

reader.read_raw()

record = Record(Raw2Record.settings.globalworkdir, reader.caseName, buses, machines, loads, trafos)
record.writeVoltages()
record.writeMachines()
record.writeLoads()
record.writeTrafos()
