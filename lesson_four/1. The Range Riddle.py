#Task 1: The Range Riddle
import random

days = ["Monday" , "Tuesday", "Wednesday", "Thursday", "Friday"]
moods = ['Sad' , 'Energetic', 'Happy', 'Calm', 'Vibrant']

for i in range(len(days)):
        day = days[i]
        mood = random.choice(moods)
        print("You are feeling ", mood, "on " + (day)) 
        
