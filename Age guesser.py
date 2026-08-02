from datetime import date

while 1:
    Birth_year = input("What is your birth year")
    try:
        Birth_year = int(Birth_year)
        break
    except ValueError:
        print("Please enter a valid Year")

while 1:
    Birth_Month = input("What is your birth Month")
    try:
        Birth_Month = int(Birth_Month)
        break
    except ValueError:
        print("Please enter a valid Month")

while 1:
    Birth_day = input("What is your birth Day")
    try:
        Birth_day = int(Birth_day)
        break
    except ValueError:
        print("Please enter a valid Day")

date = date.today()
print(f"You are {date.year - Birth_year} years, {date.month - Birth_Month} months, and {date.day - Birth_day} days old.")