#Importing the modules
from datetime import datetime, timedelta


#Current timespan
current_time = datetime.now()
print(current_time)

'''

    Output: datetime.datetime(2020, 2, 28, 19, 43, 55, 324598)

'''


#Date in yyyy-mm-dd_HH_MM_SS Format
current_date = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')

'''

    Output: '2020-02-28_19_44_56'

'''


# Operations with Datetime function
# To find the minimum and maximum year value
import datetime
datetime.MINYEAR
datetime.MAXYEAR

'''
    Output
        MinYear: 1
        MaxYear: 9999

'''


# Datetime function to print today's date
datetime.date.today()

'''
    Output
    datetime.date(2020, 8, 24)
'''


# Functions to print today's date in different format
# - Separated Date yyyy-mm-dd format
datetime.date.today().strftime("%Y-%m-%d")

'''
    Output
        '2020-08-24'
'''


# - Separated dd-mm-yyyy format
datetime.date.today().strftime("%d-%m-%Y")

''''
    Output:
        '24-08-2020'
'''


# Current Day -> dd format
>>> datetime.date.today().strftime("%d")

''''
    Output:
        '24'
'''


# Current Month -> mm format
>>> datetime.date.today().strftime("%m")

''''
    Output:
        '08'
'''


# Current Year -> yy format
>>> datetime.date.today().strftime("%y")

''''
    Output:
        '20'
'''


# Current Year -> yyyy format
>>> datetime.date.today().strftime("%Y")

''''
    Output:
        '2020'
'''


# Current Date --> dd-Mon-yyyy format
>>> datetime.date.today().strftime("%d-%b-%Y")

''''
    Output:
        '24-Aug-2020'
'''


# Current Date --> dd-Month-yyyy format
>>> datetime.date.today().strftime("%d-%B-%Y")

''''
    Output:
        '24-August-2020'
'''


# Current Date and Timestamp
>>> from datetime import datetime
>>> datetime.now()

''''
    Output:
        datetime.datetime(2020, 8, 24, 10, 49, 33, 990280)
'''


# Current Date and time in YYYY-MM-DD hh:mm:ss format
>>> datetime.now().strftime("%Y-%d-%m %H:%M:%S")

''''
    Output:
        '2020-24-08 10:50:54'
'''


# Strip date from timestamp data
>>> datetime.now().strftime("%Y-%d-%m")

''''
    Output:'2020-24-08'
'''


# Strip the time data from timestamp
>>> datetime.now().strftime("%H:%M:%S")

''''
    Output:
        '10:51:14'
'''

# Conv string to the to date
# b -> represents the acronym for the month name
# B -> represents the full month name
>>> dt = "24 Aug 2020"
>>> datetime.strptime(dt, "%d %b %Y")

''''
    Output:
        datetime.datetime(2020, 8, 24, 0, 0)
'''


# EPOCH TIME
>>> import time
>>> time.time()

''''
    Output:
1598249442.2663243
'''

# Tine in local format
>>> time.localtime()

''''
    Output:
time.struct_time(tm_year=2020, tm_mon=8, tm_mday=24, tm_hour=11, tm_min=41, tm_sec=59, tm_wday=0, tm_yday=237, tm_isdst=0)
'''

Index 	Attributes 	Values
0 	tm_year 	2020
1 	tm_mon 	    1 to 12  # 8 = August
2 	tm_mday 	1 to 31  # Today'date = 24
3 	tm_hour 	0 to 23  # Hour = 11
4 	tm_min 	    0 to 59  # Minute = 41   
5 	tm_sec 	    0 to 61 (60 or 61 are leap-seconds)
6 	tm_wday 	0 to 6 (0 is Monday)
7 	tm_yday 	1 to 366 (Julian day) # Day from 1st Jan, 24th August = 237 calerndar day
8 	tm_isdst 	-1, 0, 1, -1 means library determines DST


# Convert the local time to Day Name, Day and Year
>>> time.asctime(time.localtime(time.time()))

''''
    Output:
        'Mon Aug 24 11:41:59 2020'
'''

# Print the calender for the month
>>> cal_mon = calendar.month(2020,2)
>>> print(cal_mon)

''''
    Output:
   February 2020
        Mo Tu We Th Fr Sa Su
                        1  2
         3  4  5  6  7  8  9
        10 11 12 13 14 15 16
        17 18 19 20 21 22 23
        24 25 26 27 28 29
'''