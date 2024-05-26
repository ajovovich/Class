# # Task 1: Identify the Greatest

# x = float(input("Enter number here")) #I used float incase the user decided to be fancy and input a decimal
# y = float(input("Enter number here"))
# z = float(input("Enter number here"))

# if x > y and x > z:
#     print(x ,"is the greatest number")
# elif y > z and y > x:
#     print(y ,"is the greatest number")
# elif z > x and z > y:
#     print(z ,"is the greatest number")
# else:
#     print("There is no greatest number")

# # # Task 2: Identify the smallest number
# x = float(input("Enter number here"))
# y = float(input("Enter number here"))
# z = float(input("Enter number here"))
# if x < y and x < z:
#     print(x ,"is the smallest number")
# elif y < z and y < x:
#     print(y ,"is the smallest number")
# elif z < x and z < y:
#     print(z ,"is the smallest number")
# else:
#     print("There is no smallest number")

# # Task 3: Equality Check

# x = float(input("Enter number here"))
# y = float(input("Enter number here"))
# z = float(input("Enter number here"))

# if x == y or x == z and y > z:
#     print(x,"is the shared value",y,"is the greatest number", z,"is the smallest number")
# elif x == y or x ==z and z > y:
#     print(x,"is the shared value", z,"is the greatest value",y,"is the smallest value")
# elif y == x or y == z and x > z:
#     print(y,"is the shared value",x,"is the greatest value",z,"is the smallest value")
# elif y == x or y == z and z > x:
#     print(y,"is the shared value",z,"is the greatest value", x,"is the smallest value")
# elif z == x or z == y and x > y:
#     print(z,"is the shared value",x,"is the greateast value",y,"is the smallest value")
# else:
#     print(z,"is the shared value",y,"is the greatest value",x,"is the smalelst value") 
# I feel like there is a simpler more efficient way to do this, but this is what i created off the top of my head

year = int(input("enter year here"))

if year%400 == 0 or year%4 == 0 and not year%100 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")