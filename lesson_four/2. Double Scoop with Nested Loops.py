#Task 1: Your Mood Tracker:
import random

days = ["monday" , "tuesday", "wednesday", "thursday", "friday"]
times = ['morning', 'afternoon', 'evening']
moods = ['sad' , 'energetic', 'happy', 'calm', 'vibrant']

for i in range(len(days)):
    for j in range(len(times)):
        day = days[i]
        time = times[j]
        mood = random.choice(moods)
        print("On ", day, " " + time  + " you were feeling ", mood)