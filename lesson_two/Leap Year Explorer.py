# Task 1: Leap Year Checker

year = int(input("enter year here"))

if year%400 == 0 or year%4 == 0 and not year%100 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")