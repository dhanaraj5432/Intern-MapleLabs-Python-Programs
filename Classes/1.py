import copy

daysInMonth = {1: 31,
         2: 28,
         3: 31,
         4: 30,
         5: 31,
         6: 30,
         7: 31,
         8: 31,
         9: 30,
         10: 31,
         11: 30,
         12: 31}

nameOfMonth = {1: "January",
         2: "Feburary",
         3: "March",
         4: "April",
         5: "May",
         6: "June",
         7: "July",
         8: "August",
         9: "September",
         10: "October",
         11: "November",
         12: "December"}


class Date(object):
    """Attributes"""
date = Date()
date.month = 1
date.day = 15
date.year = 2022


def incDateFun(date, incDays):

    date_ = copy.deepcopy(date)

    while True:
        daysInMonth[2] = 28
        if (date_.year % 4 == 0):
            daysInMonth[2] = 29
        elif (date_.month != 2):
            pass

        days_left = daysInMonth[date_.month] - date_.day

        if incDays<= days_left:
            date_.day += incDays
            break
        elif incDays== 0:
            date_.day = daysInMonth[date_.month]
            break
        elif incDays< 0:
            date_.day = daysInMonth[date_.month] + incDays
            break
        else:
            incDays-= daysInMonth[date_.month]
            date_.month += 1

        if date_.month > 12:
            date_.year += 1
            date_.month = 1

    if ((date_.year - 1) % 4 == 0) and date_.month != 2:
        date_.day -= 1

    return date_

newDate = incDateFun(date, 30)

print (f"{date} {nameOfMonth[date.month]} {date.day} {date.year}")
print (f"{newDate} {nameOfMonth[newDate.month]} {newDate.day} {newDate.year}")