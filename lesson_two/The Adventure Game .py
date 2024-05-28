#Task 1: Code Correction:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

#Task 2: Setting the Scene:

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    choice = input("light a torch or proceed in the dark")
    if choice == "light a torch":
        print("You light a torch, illuminating the cave seeing the treasure and traps")
    else:
        print("You move forward in the dark, and falling into the pit trap. GAME OVER")

#Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "Do nothing":
        pass
    else:
        print("You found a boat!")
elif place == "cave":
    choice = input("light a torch or proceed in the dark")
    if choice == "light a torch":
        print("You light a torch, illuminating the cave seeing the treasure and traps")
    else:
        print("You move forward in the dark, and falling into the pit trap. GAME OVER")
