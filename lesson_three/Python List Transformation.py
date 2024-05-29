# Task 1:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort() 
print(grades)

# Task 2:
average = sum(grades)/len(grades)
print("Average of grades:", average)

#Task 3:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades[2],grades[4],grades[8] = "Failure", "Failure", "Failure"
print(grades)