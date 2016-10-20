"""Script to generate one case using NordPool data."""
import os
import sys
from datetime import date
from nordic44.nordpool import NordPool

PSSE = "C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE)
os.environ["PATH"] += ";" + PSSE

from nordic44.n44 import N44

user = "NTNU"
passwd = ""

nord = NordPool(date(2016, 3, 4))

nord.read_data_from_ftp(user, passwd)
nord.write_data_to_excel()

n44 = N44(nord.data)
n44.update_raw_files()
