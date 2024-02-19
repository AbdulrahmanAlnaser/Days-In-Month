def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def Days_in_months(month, year):
    Days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and leap_year(year):
        return 29
    else:
        return Days[month - 1]

month = int(input("Please enter the month: "))
year = int(input("Please enter the year: "))
print(f"This month contains {Days_in_months(month, year)} days.")


