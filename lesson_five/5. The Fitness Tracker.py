activity = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]


def calories_burned(duration):
        return duration*3.5

y = 0
total = 0
x = 0
activities = ""
for i in activity:
    activities = activities + i + " "
    x = calories_burned(duration[y]) + x
    y = y + 1
print(activities + "in total burnt:", x, "calories")
