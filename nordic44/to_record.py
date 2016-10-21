"""Module containing the record class"""
import os

class Record():
    '''Class defining how Modelica record file is created.'''

    def __init__(self, workdir, case_name, buses, machines, loads, trafos):
        '''
        Constructor:
            - Store dictionary of buses
        '''
        self.workdir = workdir
        self.buses = buses
        self.machines = machines
        self.loads = loads
        self.trafos = trafos
        self.case_name = case_name
        assert os.path.isdir(workdir)

    def write_voltages(self):
        """Method for writing voltages."""
        file = open(self.workdir + r'/%s_Voltages.mo' % (self.case_name), 'w')
        file.write('record %s_voltages\n   extends Modelica.Icons.Record;\n' % (self.case_name))
        for key in self.buses.keys():
            file.write('// Bus number %s\n' % (key))
            file.write('   parameter Real V%s = %f; \n' % (key, self.buses[key]['voltage']))
            file.write('   parameter Real A%s = %f; \n' % (key, self.buses[key]['angle']))
        file.write(r'end %s_voltages;' % (self.case_name))
        file.close()

    def write_machines(self):
        """Write Machines."""
        file = open(self.workdir + r'/%s_Machines.mo' % (self.case_name), 'w')
        file.write('record %s_machines\n   extends Modelica.Icons.Record;\n' % (self.case_name))
        for machine in self.machines.keys():
            file.write('// Machine %s\n' % (machine))
            file.write('   parameter Real P%s = %f; \n' % (machine, self.machines[machine]['P']))
            file.write('   parameter Real Q%s = %f; \n' % (machine, self.machines[machine]['Q']))
        file.write(r'end %s_machines;' % (self.case_name))
        file.close()

    def write_loads(self):
        """Write loads."""
        file = open(self.workdir + r'/%s_Loads.mo' % (self.case_name), 'w')
        file.write('record %s_loads\n   extends Modelica.Icons.Record;\n' % (self.case_name))
        for load in self.loads.keys():
            file.write('// Load %s\n' % (load))
            file.write('   parameter Real PL%s = %f; \n' % (load, self.loads[load]['P']))
            file.write('   parameter Real QL%s = %f; \n' % (load, self.loads[load]['Q']))
        file.write(r'end %s_loads;' % (self.case_name))
        file.close()

    def write_trafos(self):
        """Write trafos."""
        file = open(self.workdir + r'/%s_Trafos.mo' % (self.case_name), 'w')
        file.write('record %s_trafos\n   extends Modelica.Icons.Record;\n' % (self.case_name))
        for trafo in self.trafos.keys():
            file.write('// 2WindingTrafo %s\n' % (trafo))
            file.write('   parameter Real t1_%s = %f; \n' % (trafo, self.trafos[trafo]['t1']))
            file.write('   parameter Real t2_%s = %f; \n' % (trafo, self.trafos[trafo]['t2']))
        file.write(r'end %s_trafos;' % (self.case_name))
        file.close()
