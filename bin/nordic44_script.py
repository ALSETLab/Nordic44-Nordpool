"""Script to update cases using NordPool data."""
import os
import argparse

from datetime import datetime
from nordic44 import utilities

def parse_date(date):
    """Function to parse dates."""
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(date + " is not the correct date format")


if __name__ == "__main__":
    parser = (
              argparse.ArgumentParser(
                            description="Get Nordic44 data from Nordpool"))
    parser.add_argument("start_date",
                        help='Date to retrieve on format YYYY-mm-dd')
    parser.add_argument('-u', '--user', nargs=1,
                        help='Nordpool ftp user name')
    parser.add_argument('-p', '--passwd', nargs=1,
                        help='Nordpool ftp password')
    parser.add_argument('-e', '--end_date', nargs=1,
                        help='End date if a range of dates are downloade')
    parser.add_argument('-o', '--out_dir', nargs=1,
                        help="Folder where the results should be store, default is cwd")
    parser.add_argument('--no-psse', action="store_true",
                        help="If one does not want to store the data to raw")
    parser.add_argument('-R', '--records', action="store_true",
                        help="If one wants to store the data to records")
    args = parser.parse_args()
    
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
    
    utilities.data_from_nordpool(start_date=start_date, user=user, passwd=passwd,
                       out_dir=out_dir, psse=not args.no_psse,
                       end_date=end_date,records=args.records)
