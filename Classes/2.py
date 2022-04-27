import datetime
from datetime import date

weekMap = {0: "Monday",
         1: "Tuesday",
         2: "Wednesday",
         3: "Thursday",
         4: "Friday",
         5: "Saturday",
         6: "Sunday"}


class Time(object):
    now = datetime.datetime.now()

    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)


def birthdayDetails(birthday):
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1

    birthday_ = Time(today.year, birthday.month, birthday.day).date
    tillBirthday = str(birthday_ - today).split()

    if len(tillBirthday) > 1:
        days = int(tillBirthday[0])
        time = tillBirthday[2].split(":")
    else:
        days = 365
        time = tillBirthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print (f"You are {age} years old; Your next birthday is in {days}:d:{hours}h:{mins}m:{secs}s ")


today = Time().now
birthday = Time(2000, 12, 26).date

dayOfWeek = weekMap[today.weekday()]
todayDate = date.today().strftime("%d/%m/%Y")

print()
print (f"Today's date is {todayDate} and day of the week is {dayOfWeek}")
birthdayDetails(birthday)
print()