#Task 1:Cdoe a function to calculate the average grade
grades = [86, 93, 80, 98, 82, 76, 79, 64 ]

def grade_analyzer(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

#Task 2: Implement a function to find the highest and lowest grade
   
def grade_highest(grades):
    highest = max(grades)
    return highest

def grade_lowest(grades):
    lowest = min(grades)
    return lowest

#Task 3: Create a feature that categorizes grades into letter grades

def letter_grades(num):
    letter = None
    if num < 60:
        letter = 'F'
    elif num < 70:
        letter = 'D'
    elif num < 80: 
        letter = 'C'
    elif num < 90:
        letter = 'B'
    else:
        letter = 'A'
    return letter

converted_grades = [letter_grades(num) for num in grades]

print(converted_grades)

grade_average = grade_analyzer(grades)
print(f"The average grade is {grade_average:.2f}")

highest = grade_highest(grades)
lowest = grade_lowest(grades)
print("The highest grade is ", highest, "While the lowest grade is ", lowest)
