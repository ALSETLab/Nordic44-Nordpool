"""Script to update cases using NordPool data."""
import os
import sys
import argparse
from datetime import timedelta
from datetime import datetime
from nordic44.nordpool import NordPool

def parse_date(date):
    try:
        return datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        raise ValueError(date + " is not the correct date format")

def main(argv):
    parser = (
             argparse.ArgumentParser(
                        description="Get Nordic44 data from Nordpool"))
    parser.add_argument("start_date",
                        help='Date to retrieve on format YYYY-mm-dd')
    parser.add_argument('-u', '--user',  nargs=1,
                        help='Nordpool ftp user name')
    parser.add_argument('-p', '--passwd',  nargs=1,
                        help='Nordpool ftp password')
    parser.add_argument('-e', '--end_date', nargs=1,
                        help='End date if a range of dates are downloade')
    parser.add_argument('-o', '--out_dir', nargs=1,
                        help="Folder where the results should be store, default is cwd")
    parser.add_argument('--no-psse', action="store_true",
                        help="If one does not want to store the data to raw")
    args = parser.parse_args()
    
    cwd = os.getcwd()
    start_date = parse_date(args.start_date)    
  
    if args.user:
        user = args.user[0]
    if args.passwd:
        passwd = args.passwd[0]
    if args.end_date:
        end_date = parse_date(args.end_date[0])
    else:
        end_date = start_date
    if args.out_dir:
        out_dir = args.outdir[0]
    else:
        out_dir = os.getcwd()
        
    os.chdir(out_dir)
    
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
        
        if not args.no_psse:
            from nordic44.n44 import N44
            n44 = N44(nord.data, out_dir=out_dir)
            n44.update_raw_files()
        os.chdir("..")
    os.chdir(cwd)

if __name__ == "__main__":
    main(sys.argv)