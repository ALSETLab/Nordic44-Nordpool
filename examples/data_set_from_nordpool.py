"""Script to update cases using NordPool data."""
import os
import sys
from datetime import date
from datetime import timedelta
from nordpool import NordPool

# PSSE = "C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
# sys.path.append(PSSE)
# os.environ["PATH"] += ";" + PSSE

# from n44 import N44

user = "NTNU"
passwd = ""

# Find current directory
encoding = sys.getfilesystemencoding()
cwd = os.path.dirname(os.path.abspath(__file__))

# Location of basecase file
basecase = os.path.join(
    cwd.encode(encoding), "..", "01_PSSE_Resources",
    "Models", "PSSE Base case",
    "N44_BC.sav")

basecase = os.path.normpath(basecase)

start_date = date(2016, 1, 1)
end_date = date(2016, 10, 15)

for i in range((end_date-start_date).days + 1):
    date = start_date + timedelta(i)
    date_str = date.strftime("%Y%m%d")

    dir_str = "N44_" + date_str
    
    try:
        os.makedirs(dir_str)
    except OSError:
        pass
    os.chdir(dir_str)

    nord = NordPool(date)

    nord.read_data_from_ftp(user, passwd)
    nord.write_data_to_excel()

    # n44 = N44(nord.data, basecase)
    # n44.update_raw_files()
    # os.chdir("..")
