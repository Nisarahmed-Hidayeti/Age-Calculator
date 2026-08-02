

while 1:
    Birth_year = input("What is your birth year")

    try:
        Birth_year = int(Birth_year)
        break
    except ValueError:
        print("Please enter a valid date")



Birth_Month = input("What is your birth Month")
Birth_day = input("What is your birth day")
