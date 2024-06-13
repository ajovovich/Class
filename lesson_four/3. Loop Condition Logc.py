#Task 1: Loop Condition Exploration

power = 35
tries = 0
while True:
    if power > 10:
        tries = tries + 1
    print("You are too strong")
    if tries > 4:
        break

#Task 2: Conditional Exit

power = 35
power_level_required = 100
while power != power_level_required:
        power = (power + 65)
        print("You are strong like guerilla")
        