"""Read data from Nordpool and store it in various formats."""
import os
from datetime import timedelta
from nordic44.nordpool import NordPool

def data_from_nordpool(start_date, user, passwd, out_dir=None, end_date=None,
                       records=False, psse=True):
    """The main function."""
    if not end_date:
        end_date = start_date

    cwd = os.getcwd()
    if not out_dir:
        out_dir = cwd
    
    # I know there should be no imports here,
    # but it is a simple hack to run under linux
    if psse:
        from nordic44.n44 import N44
        raw_dir = os.path.join(out_dir, "PSSE_Resources")
        os.mkdir(raw_dir)
        if records:
            from nordic44.readraw import Reader
            from nordic44.torecord import Record
            record_dir = os.path.join(out_dir, "Records")
            os.mkdir(record_dir)
                    
    for i in range((end_date-start_date).days + 1):
        date = start_date + timedelta(i)
        date_str = date.strftime("%Y%m%d")

        dir_str = "N44_" + date_str

        nord = NordPool(date)

        nord.read_data_from_ftp(user, passwd)
        
        tmp_raw = os.path.join(raw_dir, dir_str)
        os.mkdir(tmp_raw)
        nord.write_data_to_excel(tmp_raw)

        if psse:
            n44 = N44(nord.data)

            n44.update_raw_files(out_dir=tmp_raw)
            if records:
                reader = Reader(tmp_raw)
                lista = reader.get_list_of_raw_files()
                tmp_record_dir = os.path.join(record_dir, dir_str)
                for raw in lista:
                    reader.open_raw(raw)
                    reader.read_raw()
                    record = Record(tmp_record_dir,
                                    reader.case_name,
                                    reader.buses, reader.machines,
                                    reader.loads, reader.trafos)
                    record.write_voltages()
                    record.write_machines()
                    record.write_loads()
                    record.write_trafos()
                    record.close_record()