#Task 1: Random Choice Game
import random

item_list = ['Sword', 'Bow', 'Staff', 'Wand', 'Dagger']

user_input = input("Guess what item was selected")
item = random.choice(item_list)

if user_input == item:
    print("You guessed " , user_input, "and the item was ", item, ", you are correct!")
else:
    print("You guessed ", user_input, "and the item was ", item, ", you did not guess correctly")