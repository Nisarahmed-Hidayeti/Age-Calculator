from datetime import date

datenow = date.today()

while 1:
    Birth_year = input("What is your birth year")
    try:
        Birth_year = int(Birth_year)
        if(0 < Birth_year <= datenow.year):
            break
        else:
            print("Please enter a valid Year")
    except ValueError:
        print("Please enter a valid Year")

while 1:
    Birth_Month = input("What is your birth Month")
    try:
        Birth_Month = int(Birth_Month)
        if(0 < Birth_Month < 13):
            break
        else:
            print("Please enter a valid Month")
    except ValueError:
        print("Please enter a valid Month")

while 1:
    Birth_day = input("What is your birth Day")
    try:
        Birth_day = int(Birth_day)
        break
    except ValueError:
        print("Please enter a valid Day")

birth_date = date(Birth_year, Birth_Month, Birth_day)

ageyear = datenow.year - Birth_year
agemonth = datenow.month - Birth_Month
ageday = datenow.day - Birth_day

if agemonth < 0:
    ageyear -= 1
    agemonth += 12

if ageday < 0:
    agemonth -= 1

    if datenow.month == 1:
        previous_month = 12
        previous_year = datenow.year - 1
    else:
        previous_month = datenow.month - 1
        previous_year = datenow.year

    if previous_month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_previous_month = 31
    elif previous_month in [4, 6, 9, 11]:
        days_in_previous_month = 30
    else:
        if previous_year % 4 == 0:
            days_in_previous_month = 29
        else:
            days_in_previous_month = 28

    ageday += days_in_previous_month

print(f"You are {ageyear} years, {agemonth} months, and {ageday} days old.")

alive = datenow - birth_date
print(f"You are alive for {alive.days} days")