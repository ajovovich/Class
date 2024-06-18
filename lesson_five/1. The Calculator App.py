# #Task: 1

a = 5
b = 3

def addition(a = 5, b = 3):
    return a + b, a - b, a * b, a / b
    
# def subtraction(a, b):
#     return a - b

# def multiplication(a, b):
#     return a * b

# def divison(a, b):
#     return a / b 

operation = addition
print (operation)

# #Task: 2 Adding in user input and operational choice


# value_1 = int(input("Enter desired number here"))
# value_2 = int(input("Enter second value here"))
# choice = input("Choose operation choice (Addition, Subtraction, Multiplication, Division).").lower()
# def addition(value_1, value_2):
#     return value_1 + value_2

# def subtraction(value_1, value_2):
#     return value_1 - value_2

# def multiplication(value_1, value_2):
#     return value_1 * value_2

# def division(value_1, value_2):
#     return value_1 / value_2

# if choice == "addition":
#     result = addition(value_1, value_2)
#     print("The numbers added = ", result)

# elif choice == "subtraction":
#     result = subtraction(value_1, value_2)
#     print("The numbers subtracted = ", result)

# elif choice == "multiplication":
#     result = multiplication(value_1, value_2)
#     print("The numbers mulitplied = ", result)

# elif choice == "division":
#     result = division(value_1, value_2)
#     print("The numbers divided = ", result)

# # #Task: 3 Fixing ZeroDivisionError and other errors

# value_1 = int(input("Enter desired number here"))
# value_2 = int(input("Enter second value here"))
# choice = input("Choose operation choice (Addition, Subtraction, Multiplication, Division).").lower()
# def addition(value_1, value_2):
#     return value_1 + value_2

# def subtraction(value_1, value_2):
#     return value_1 - value_2

# def multiplication(value_1, value_2):
#     return value_1 * value_2

# def division(value_1, value_2):
#     return value_1 / value_2 if value_2 else 0 #Added if value_2 else 0 to fix the ZeroDivisionError

# if choice == "addition":
#     result = addition(value_1, value_2)
#     print("The numbers added =", result)

# elif choice == "subtraction":
#     result = subtraction(value_1, value_2)
#     print("The numbers subtracted =", result)

# elif choice == "multiplication":
#     result = multiplication(value_1, value_2)
#     print("The numbers mulitplied =", result)

# elif choice == "division":
#     result = division(value_1, value_2)
#     print("The numbers divided =", result)



