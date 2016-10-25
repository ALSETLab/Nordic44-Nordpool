"""Module containing the record class"""
import os

class Record():
    '''Class defining how Modelica record file is created.'''

    def __init__(self, workdir, raw_file_path, case_name, buses, machines, loads, trafos):
        '''
        Constructor:
            - Store dictionary of buses
            - Open a record file
            - Write the beginning of the file
        '''

        self.buses = buses
        self.machines = machines
        self.loads = loads
        self.trafos = trafos
        self.case_name = case_name
        assert os.path.isfile(raw_file_path)
        self.record_path = workdir
        if not os.access(self.record_path, os.F_OK):
            os.mkdir(self.record_path)
        self.record_file = open(self.record_path + r'/%s.mo' % self.case_name, 'w+')
        self.record_file.write('record PF_results\n //Power flow results for the snapshot %s\n \n' % self.case_name +
                               'extends Modelica.Icons.Record; \n')

    def write_voltages(self):
        """Method for writing voltages."""

        self.record_file.write('record Voltages\n')
        for key in self.buses.keys():
            self.record_file.write('// Bus number %s\n' % key)
            self.record_file.write('   parameter Real V%s = %f; \n' % (key, self.buses[key]['voltage']))
            self.record_file.write('   parameter Real A%s = %f; \n' % (key, self.buses[key]['angle']))
        self.record_file.write('end Voltages;\n')

    def write_machines(self):
        """Write Machines."""
        self.record_file.write('record Machines\n')
        for machine in self.machines.keys():
            self.record_file.write('// Machine %s\n' % machine)
            self.record_file.write('   parameter Real P%s = %f; \n' % (machine, self.machines[machine]['P']))
            self.record_file.write('   parameter Real Q%s = %f; \n' % (machine, self.machines[machine]['Q']))
        self.record_file.write('end Machines;\n')

    def write_loads(self):
        """Write loads."""
        self.record_file.write('record Loads\n')
        for load in self.loads.keys():
            self.record_file.write('// Load %s\n' % load)
            self.record_file.write('   parameter Real PL%s = %f; \n' % (load, self.loads[load]['P']))
            self.record_file.write('   parameter Real QL%s = %f; \n' % (load, self.loads[load]['Q']))
        self.record_file.write('end Loads;\n')

    def write_trafos(self):
        """Write trafos."""
        self.record_file.write('record Trafos\n')
        for trafo in self.trafos.keys():
            self.record_file.write('// 2WindingTrafo %s\n' % trafo)
            self.record_file.write('   parameter Real t1_%s = %f; \n' % (trafo, self.trafos[trafo]['t1']))
            self.record_file.write('   parameter Real t2_%s = %f; \n' % (trafo, self.trafos[trafo]['t2']))
        self.record_file.write(r'end Trafos;\n')

    def close_record(self):
        """Close the file"""
        self.record_file.write('Voltages voltages;\n')
        self.record_file.write('Machines machines;\n')
        self.record_file.write('Loads loads;\n')
        self.record_file.write('Trafos trafos;\n')
        self.record_file.write('end PF_results;')
        self.record_file.close()
