"""Script to update cases using NordPool data from excel."""
import os
import sys
from datetime import  date
from nordpool import NordPool

PSSE = "C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE)
os.environ["PATH"] += ";" + PSSE

from n44 import N44


# Find current directory
encoding = sys.getfilesystemencoding()
cwd = os.path.dirname(os.path.abspath(__file__))

# Find excel files
files_path = os.path.join(
    cwd.encode(encoding), "..", "01_PSSE_Resources",
    "Snapshots", "N44_20150101")

# Location of basecase file
basecase = os.path.join(
    cwd.encode(encoding), "..", "01_PSSE_Resources",
    "Models", "PSSE Base case",
    "N44_BC.sav")

basecase = os.path.normpath(basecase)

no_prod = os.path.join(files_path, "Production_NO.xlsx")
no_con = os.path.join(files_path, "Consumption_NO.xlsx")
no_ex = os.path.join(files_path, "Exchange_NO.xlsx")

se_prod = os.path.join(files_path, "Production_SE.xlsx")
se_con = os.path.join(files_path, "Consumption_SE.xlsx")
se_ex = os.path.join(files_path, "Exchange_SE.xlsx")

fi_prod = os.path.join(files_path, "Production_FI.xlsx")
fi_con = os.path.join(files_path, "Consumption_FI.xlsx")
fi_ex = os.path.join(files_path, "Exchange_FI.xlsx")

nord = NordPool(date(2015, 1, 1))

nord.read_data_from_excel(no_prod, se_prod, fi_prod,
                          no_con, se_con, fi_con,
                          no_ex, se_ex, fi_ex)
# nord.write_data_to_excel()

n44 = N44(nord.data, basecase)
n44.update_raw_files()
