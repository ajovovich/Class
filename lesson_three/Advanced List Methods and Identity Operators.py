# Task 1: Given the two lists:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = submitted[0] in attended #True
print(both , ("Alice submitted and attended"))
both = submitted[1] in attended #False
print(both , ("Bob submitted but did not attend"))
both = submitted[2] in attended #True
print(both , ("Charlie submitted and attended"))
both = submitted[3] in attended #False
print(both , ("David submitted but did not attend"))

#Unsure of how to compile or if there is  a way to check both lists and return unique resutls for all

# Task 2: 
if submitted == attended:
    print("The two lists are the same")
else:
    print("The two lists are not identical")

# Task 3:
attended.remove("Eve") , attended.remove("Frank") #['Charlie', 'Alice']
print(attended)
