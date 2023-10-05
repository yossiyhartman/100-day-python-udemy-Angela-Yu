

def is_leap_year(year):
  if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
    print("Given year is a leap Year")
  else:
    print("Given year is not a leap Year")

def getDaysInMonth(year, month):

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[1] += 1

    print(days_in_month[month - 1])


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))

getDaysInMonth(year, month)



