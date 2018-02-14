
import random
import string
import csv
import calendar
import time

# Write a python code to create a data set and write it down to csv file.
# Step 1 Create a dataset consists of 10 rows
# 1. Create a csv file and write it down
rt_file = open("random_fuse_sub.csv", 'w')
wr = csv.writer(rt_file, delimiter='|')
list_col = []

time1 = time.clock()
# 2. Create 1 column and iterate for 10 times
for x in range (10):
    # add a uniqueID
    uniqueid = 'MT_' + str(''.join(random.sample(string.digits * 6, 6))) + '_' + str(random.choice(string.ascii_uppercase) + random.choice(string.digits))
    list_col.append(uniqueid)

    # add a country
    country_list = {'JAP': 'Japanese', 'KOR': 'Korean', 'IND': 'Hindi', 'CHI': 'Chinese', 'USA': 'English',
                    'FRA': 'French', 'GER': 'German', 'AUS': 'English'}
    country_name = random.choice(list(country_list.keys()))
    list_col.append(country_name)

    # add a name
    name_list = {'JAP': 'Hanako Tanaka', 'KOR': 'Kyung-min Lee', 'IND': 'Indrani Singh', 'CHI': 'Jinping Xi', 'USA': 'Barack Obama',
                    'FRA': 'Lucie Godfroy', 'GER': 'Angela Merkel', 'AUS': 'Malcolm Turnbull'}
    name = name_list.get(country_name)
    list_col.append(name)

    # add a language
    language = country_list.get(country_name)
    list_col.append(language)

    # add a random birth date between 1991/8 - 1997/2
    year = random.randrange(1991,1997,1)
    if year == 1991:
        month_list = ['Aug','Sep','Oct','Nov','Dec']
        month = random.choice(month_list)
        if month == 'Aug':
            date = random.randrange(4,30)
        elif month == 'Sep' or 'Nov':
            date = random.randrange(1,30)
        else:
            date = random.randrange(1,31)
        randomdate = str(month) + '-' + str(date) + '-' + str(year)
        list_col.append(randomdate)
    elif year == 1997:
        month_list2 =  ['Jan','Feb']
        if month == 'Jan':
            date = random.randrange(1,31)
        else:
            date = random.randrange(1,28)
        randomdate = str(month) + '-' + str(date) + '-' + str(year)
        list_col.append(randomdate)
    else:
        month_list3 = ['Jan','Feb','Mar','Apr','May','Jul','Jun','Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month = random.choice(month_list3)
        # For month of Feb, to check if year is leap or not
        if not calendar.isleap(year):
            date = random.randrange(1,29)
        if month == 'Feb':
            date = random.randrange(1,28)
        elif month == 'Apr' or 'Jun' or 'Sep' or 'Nov':
            date = random.randrange(1,31)
        else:
            date = random.randrange(1,30)
        randomdate = str(month) + '-' + str(date) + '-' + str(year)
        list_col.append(randomdate)

    # Select the age based on the name
    age_list = {'Hanako Tanaka':'20', 'Kyung-min Lee':'23', 'Indrani Singh':'20', 'Jinping Xi':'45',
                 'Barack Obama':'53','Lucie Godfroy':'22', 'Angela Merkel':'24', 'Malcolm Turnbull':'50'}
    age = age_list.get(name)
    list_col.append(age)

    # Calculate the range of the random value such that it falls within the height range and then apply conversion and format into Feets-Inches
    feet = random.randrange(5,7)
    Ft = str(feet) + 'Ft'
    Inch = random.randrange(1,12)
    In = str(Inch) + 'In'
    height = str(Ft) + ' ' + str(In)
    list_col.append(height)

    # Pick the median per capita income
    country_list = {'JAP': 41275, 'KOR': 37740, 'IND': 6572, 'CHI':15535 , 'USA': 57436,
                    'FRA': 42314, 'GER': 48111, 'AUS': 48899}
    salary = country_list.get(country_name)
    # Pick a random number within 30% of their median per capita income
    sal = salary*0.3
    sal2 = '$' + str(random.randrange(1, int(sal)))
    list_col.append(sal2)

    wr.writerow(list_col)
    del list_col[:]

    time2 = time.timer()
    time = time2-time1
    print ('the time taken for the program to create 10 records is' + str(time))
