'''
ID: yezhang2
LANG: PYTHON3
TASK: friday
'''
yearStart = 1900
nonLeapDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK_DAYS = 7

def checkLeapYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False

    if year % 4 == 0:
        return True
    else:
        return False

def calculateWeekDays(yearRoundDays, weekDays):
    '''
    * totalDays : Represent all the 13th(s), counts from 01/01/1900
    * totalDays % 7, the remainder is the day 13 falls on, except Sunday
    * Initialize to 13, the 1st 13.
    '''
    totalDays = 0
    for days in yearRoundDays[0:-1]:
        totalDays += days
        remainder = totalDays % WEEK_DAYS
        if remainder == 0:
            weekDays[WEEK_DAYS] += 1  # Sunday
        else:
            weekDays[remainder] += 1
 
with open("friday.in", "r") as fin:
    numYears = int(fin.readline().strip('\n'))

thirteenthDays = []
yearRoundDays = [13]
for i in range(0, numYears):
    isLeapYear = checkLeapYear(yearStart + i)
    if isLeapYear:
        yearRoundDays.extend(leapDays)
    else:
        yearRoundDays.extend(nonLeapDays)

weekDays = {}
for i in range(1, 8):
    weekDays[i] = 0

calculateWeekDays(yearRoundDays, weekDays)

outputSeq = [6, 7, 1, 2, 3, 4, 5]
with open("friday.out", "w") as fout:
    for day in outputSeq[0:-1]:
        fout.write(str(weekDays[day]) + ' ')
    friday = outputSeq[len(outputSeq) - 1]
    fout.write(str(weekDays[friday]) + '\n')

