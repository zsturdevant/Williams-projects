# Compute and print the current day of the week.

# import module to compute the seconds since midnight of 1/1/1970:
from time import time

def UTCDay(timeval):
    """Takes as input UTC time value (float), and returns the
    number of the day of the week (integer between 0 and 6 inclusive)"""
    day = (int(time()) % (60*60*24)) % 7
    return dayUTC

def localDay(timeval, offset):
    """Takes as input UTC time value  (float) and an offset (float),
    calls UTCDay to help compute the current day of the week
    for a timezone that is offset hours ahead of UTC.
    """
    localDay = ((timeval + (offset*3600)) % (60*60*24)) % 7
    return localDay

def dayOfWeek(dayNumber):
    """Takes an integer between 0 and 6 (inclusive) as input and
    returns the name of that day as a string"""
    if dayNumber == 0:
        return "Thursday"
    elif dayNumber == 1:
        return "Friday"
    elif dayNumber == 2:
        return "Saturday"
    elif dayNumber == 3:
        return "Sunday"
    elif dayNumber == 4:
        return "Monday"
    elif dayNumber == 5:
        return "Tuesday"
    elif dayNumber == 6:
        return "Wednesday"



# at this point, we have definitions necessary to support the computation
# add code, here, to print the day of the week in Williamstown (offset -5)
# according to the format described in the lab handout.

if __name__ == "__main__":
    # statements in this suite are only executed when this is run as a script:
  # run as a script?
    now = time()                   # UTC time
    dayNumber = localDay(now, -5)  # Eastern day of week number
    dayName = dayOfWeek(dayNumber) # get day name
    print("It's "+ dayName +"!")   # print it out
