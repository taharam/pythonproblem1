
import re
import random
import numpy as np
import string
from datetime import datetime

# generating uniqueID
middle = ''.join(random.sample(string.digits * 6, 6))
last = random.choice(string.ascii_uppercase) + random.choice(string.digits)
uniqueid = 'MT_' + str(middle) + '_' + str(last)
print(uniqueid)

# randomly pick the country
country_list = {'JAP': 'Japanese', 'KOR': 'Korean', 'IND': 'Hindi', 'CHI': 'Cantonese', 'USA': 'English',
                'FRA': 'French', 'GER': 'German', 'AUS': 'English'}
country_name = random.choice(list(country_list.keys()))

# Copy paste 10 first names and last names for each country randomly

# Automatically assign the language based on the country
language = country_list.get(country_name)


# Randomly set the date
def dategenerator(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return dategenerator(start, end, '%m-%d-%Y', prop)


print randomDate('2-4-1997', '8-7-1991', random.random())
ERROR

# Set age based on the current data

#
