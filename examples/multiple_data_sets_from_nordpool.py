"""Script to update cases using NordPool data."""
import os
import sys
from datetime import date

PSSE = r"C:\Program Files (x86)\PTI\PSSE33\PSSBIN"
sys.path.append(PSSE)
os.environ["PATH"] += ";" + PSSE

from nordic44 import utilities

user = "NTNU"
passwd = "qhvi779"

start_date = date(2016, 1, 1)
end_date = date(2016, 10, 15)

utilities.data_from_nordpool(start_date=start_date, user=user, passwd=passwd,
                             end_date=end_date, records=True)
