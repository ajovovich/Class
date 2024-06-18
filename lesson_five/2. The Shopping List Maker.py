#Task 1: Write a function that lets the user add items to a list
shopping_list = []

def add_list(add_item):
    global shopping_list
    shopping_list.append(add_item)

#Task 2: Add a feature to remove items from the list

def remove_list(remove_item):
    global shopping_list
    shopping_list.remove(remove_item)


while True:
    choice = input("Would you like to remove or add an item? Type 'Done' to print your list").lower()
    if choice == "add":
        items = input("Write down items that you want to add to your shopping list")
        add_list(items)
    elif choice == "remove":
        items = input("Write down items that you want to remove from your shopping list")
        remove_list(items)
    elif choice == 'done':
        break

#Task 3: Print list in a formatted way

print(shopping_list) 