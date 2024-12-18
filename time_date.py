from datetime import date
fdate=date(2015,7,2)
ldate=date(2013,7,9)
delta=fdate-ldate
print(delta.days)

import time
millisec=int(round(time.time()*1000))
print(millisec)

import time
print(time.asctime(time.strptime('2014 50 1', '%Y %W %w')))
