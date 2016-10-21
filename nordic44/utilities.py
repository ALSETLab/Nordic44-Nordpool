"""Read data from Nordpool and store it in various formats."""
import os
from datetime import timedelta
from nordic44.nordpool import NordPool
from nordic44.readraw import Reader
from nordic44.torecord import Record


def data_from_nordpool(start_date, user, passwd, out_dir=None, end_date=None,
                       records=False, psse= True):
    """The main function."""
    if not end_date:
        end_date = start_date

    cwd = os.getcwd()
    if not out_dir:
        out_dir = cwd
    os.chdir(out_dir)

    for i in range((end_date-start_date).days + 1):
        date = start_date + timedelta(i)
        date_str = date.strftime("%Y%m%d")

        dir_str = os.path.join(out_dir, "N44_" + date_str)

        try:
            os.makedirs(dir_str)
        except OSError:
            pass
        os.chdir(dir_str)

        nord = NordPool(date)

        nord.read_data_from_ftp(user, passwd)
        nord.write_data_to_excel()

        if psse:
            from nordic44.n44 import N44
            n44 = N44(nord.data)
            n44.update_raw_files(out_dir=dir_str)
                       
            if records:
                record_dir = os.path.join(dir_str, "records")
                try:
                    os.makedirs(record_dir)
                except OSError:
                    pass
                reader = Reader(dir_str)

                lista = reader.get_list_of_raw_files()
                print ("Liste")
                print(len(lista))
                for raw in lista:
                    reader.open_raw(raw)
                    reader.read_raw()

                    record = Record(record_dir,
                                    reader.case_name,
                                    reader.buses, reader.machines,
                                    reader.loads, reader.trafos)
                    record.write_voltages()
                    record.write_machines()
                    record.write_loads()
                    record.write_trafos()
            
            os.chdir("..")
    os.chdir(cwd)