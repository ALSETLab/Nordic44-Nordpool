'''
Created on 2015-02-24
author: trabuzin at gmail dot com
'''

import os
import redirect
import psspy


class Reader():
    '''A class which defining how .raw file is read.'''

    def __init__(self, raw_file_dir):
        '''
        Constructor:
            - Store work and raw folder paths
            - Initialize PSS/E
        '''
        assert os.path.isdir(raw_file_dir) or os.path.isfile(raw_file_dir)

        self.raw_file_dir = raw_file_dir
        self.rawfilelist = []
        self.buses = {}
        self.machines = {}
        self.loads = {}
        self.trafos = {}
        self.case_name = ''
        redirect.psse2py()
        psspy.psseinit(100)

    def get_list_of_raw_files(self):
        '''
        Creates a list of available raw files
        '''
        if os.path.isdir(self.raw_file_dir):
            print(self.raw_file_dir)
            for i in os.listdir(self.raw_file_dir):
                if i.endswith(".raw"):
                    self.rawfilelist.append(i)

        else:
            self.rawfilelist.append(self.raw_file_dir)
        return self.rawfilelist

    def open_raw(self, filepath):
        '''
        Reads and opens a raw file
        '''
        ierr = psspy.readrawversion(0, '33.0', filepath)
        (_, fname) = os.path.split(filepath)
        self.case_name = fname[:-4]

        assert ierr == 0, 'Raw file cannot be opened'

    def read_raw(self):
        ''' Read the raw file.'''

        # Read bus numbers
        ierr, bus_numbers = psspy.abusint(-1, 2, 'NUMBER')

        assert ierr == 0, 'Error with reading bus numbers'

        # Reads voltage levels at buses stored in self.busNumbers
        ierr, voltage_levels = psspy.abusreal(-1, 2, 'PU')

        assert ierr == 0, 'Error reading voltage levels'

        # Reads voltage levels at buses stored in self.busNumbers
        ierr, voltage_angles = psspy.abusreal(-1, 2, 'ANGLED')

        assert ierr == 0, 'Error reading voltage angles'

        # Creates a Python dictionary containing bus numbers as keys and associates
        # a dictionary with voltage and angle to each of the keys
        for bus, voltage, angle in zip(bus_numbers[0], voltage_levels[0], voltage_angles[0]):
            self.buses[bus] = {'voltage': voltage, 'angle': angle}

        # Reads and stores bus numbers where generators are connected
        ierr, [machine_bus_numbers] = psspy.amachint(-1, 4, 'NUMBER')
        ierr, [machine_ids] = psspy.amachchar(-1, 4, 'ID')
        assert ierr == 0, 'Error reading generator bus numbers'

        # Reads and stores active and reactive powers of each generator
        ierr1, [machine_power_p] = psspy.amachreal(-1, 4, 'PGEN')
        ierr2, [machine_power_q] = psspy.amachreal(-1, 4, 'QGEN')

        assert (ierr1 == 0) and (ierr2 == 0), 'Error with reading active and reactive powers'

        # Creates a Python dictionary containing keys in form of
        # "BUSNUMBER_MACHINEID" and associates a dictionary with active and
        # reactive powers to each of the keys
        for k in range(0, len(machine_ids)):
            self.machines[(str(machine_bus_numbers[k])+'_' +
                           machine_ids[k][:-1])] = {
                               'bus': machine_bus_numbers[k],
                               'P': machine_power_p[k], 'Q': machine_power_q[k]}

        # Reads and stores bus numbers where loads are connected
        ierr, [load_bus_numbers] = psspy.aloadint(-1, 4, 'NUMBER')
        ierr, [load_ids] = psspy.aloadchar(-1, 4, 'ID')
        assert ierr == 0, 'Error reading load bus numbers'

        # Reads and stores active and reactive powers of each load
        ierr1, [load] = psspy.aloadcplx(-1, 4, 'TOTALACT')
        load_power_p = []
        load_power_q = []
        for cplxload in load:
            load_power_p.append(cplxload.real)
            load_power_q.append(cplxload.imag)

        assert ierr1 == 0, 'Error with reading active and reactive powers'

        # Creates a Python dictionary containing keys in form of
        # "BUSNUMBER_LOADID" and associates a dictionary with active and
        # reactive powers to each of the keys

        for load, bus, active, reactive in zip(
                load_ids, load_bus_numbers, load_power_p, load_power_q):
            self.loads[(str(bus)+'_' + load[:-1])] = {'bus': bus, 'P': active, 'Q': reactive}

        # Reads and stores bus numbers where 2WindingTrafos are connected
        ierr1, [two_w_trafo_from] = psspy.atrnint(-1, 1, 1, 2, 1, 'FROMNUMBER')
        ierr2, [two_w_trafo_to] = psspy.atrnint(-1, 1, 1, 2, 1, 'TONUMBER')

        assert (ierr1 == 0) and (ierr2 == 0), 'Error reading trafo bus numbers'

        # Reads and stores 2WindingTrafo ratios taking into account the primary side
        ierr1, [two_w_trafo_ratio1] = psspy.atrnreal(-1, 1, 1, 2, 1, 'RATIO')
        ierr2, [two_w_trafo_ratio2] = psspy.atrnreal(-1, 1, 1, 2, 1, 'RATIO2')

        assert (ierr1 == 0) and (ierr2 == 0), 'Error reading trafo bus numbers'

        # Creates a Python dictionary containing keys in form of
        # "BUSNUMBER_LOADID" and associates a dictionary with active and
        # reactive powers to each of the keys
        for f_bus, to_bus, ratio1, ratio2 in zip(two_w_trafo_from,
                                                 two_w_trafo_to,
                                                 two_w_trafo_ratio1,
                                                 two_w_trafo_ratio2):
            self.trafos[(
                str(f_bus) + '_' + str(to_bus))] = {'fromBus': f_bus, 'toBus': to_bus,
                                                    't1': ratio1, 't2': ratio2}
