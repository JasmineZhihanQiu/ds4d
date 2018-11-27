import time
date_str = '06/07/2018 12:34'
fmt = '%d/%m/%Y %H:%M'
time_tamp = time.strptime(date_str, fmt)
year, month, day = time_tamp[:3]
a_date = datetime.date(year, month, day)
print(a_date)