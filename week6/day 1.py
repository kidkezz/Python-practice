#The “Prime Dates” problem is a debugging challenge where you are given a piece of code with some errors. The task is to identify and correct these errors to make the code work as expected. The catch is that you are only allowed to modify a maximum of 5 lines; you cannot add or delete any lines.
#The code is designed to calculate the number of ‘lucky’ dates between two given dates. A date is considered ‘lucky’ if the numeric representation of the date (in the format DDMMYYYY) is divisible by either 4 or 7. The challenge involves understanding the logic of the code, identifying the errors, and making the necessary modifications to correct them.

#original code:
import re
month = []

def updateLeapYear(year):
    if year % 400 == 0:
        month[2] = 28
    elif year % 100 == 0:
        month[2] = 29
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        x = d1
        x = x * 100 + m1
        x = x * 1000 + y1
        if x % 4 == 0 and x % 7 == 0:
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                y1 =  y1 + 1
                m1 = m1 + 1
    return result;

for i in range(1, 15):
    month.append(31)

line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)

#modified code
import re
month = []

def updateLeapYear(year):
    # The first problem I noticed was a problem in the first 2 conditions because the days of month 2 are switched.
    # Therefore, I will modify 2 out of 5 lines. Then I examined the other lines and saw how the program calculates x.
    if year % 400 == 0:
        month[2] = 29 # line modified
    elif year % 100 == 0:
        month[2] = 28 # line modified
    elif year % 4 == 0:
        month[2] = 29
    else:
        month[2] = 28

def storeMonth():
    month[1] = 31
    month[2] = 28
    month[3] = 31
    month[4] = 30
    month[5] = 31
    month[6] = 30
    month[7] = 31
    month[8] = 31
    month[9] = 30
    month[10] = 31
    month[11] = 30
    month[12] = 31

def findPrimeDates(d1, m1, y1, d2, m2, y2):
    storeMonth()
    result = 0

    while(True):
        # The first two instructions are correct, but the last one is incorrect.
        # We need x to be in the format 00000000 and for that we need to multiply by 10000, not 1000. This is the 3rd out of 5 lines to modify.
        x = d1
        x = x * 100 + m1
        x = x * 10000 + y1 #line modified
        # The fourth line to modify is below. A lucky number is a number that can be divided by 4 or 7, not 4 and 7. This is the 4th out of 5 lines to modify.
        if x % 4 == 0 or x % 7 == 0:#line modified
            result = result + 1
        if d1 == d2 and m1 == m2 and y1 == y2:
            break
        updateLeapYear(y1)
        d1 = d1 + 1
        if d1 > month[m1]:
            m1 = m1 + 1
            d1 = 1
            if m1 > 12:
                # For the last modification, I kept looking at how the program works.
                # the month keeps adding and not updating to 1. We only need to change it to 1 so that the month will be updated to 1 in every iteration.
                y1 =  y1 + 1
                m1 = 1 #line modified
    return result

for i in range(1, 15):
    month.append(31)

line = input()
date = re.split('-| ', line)
d1 = int(date[0])
m1 = int(date[1])
y1 = int(date[2])
d2 = int(date[3])
m2 = int(date[4])
y2 = int(date[5])

result = findPrimeDates(d1, m1, y1, d2, m2, y2)
print(result)
