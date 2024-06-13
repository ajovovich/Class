# Task 1: The for Loop DJ Set

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for x in range(len(genres)):
    genre = genres[x]
    print("You are listening to track #",x, genre, "genre")

# Task 2: The Remix Artist with while

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

while range(len(genres)):
    genre = genres.pop(0)
    if genre == 'Classical':
        break
    print("You are listening to", genre, "genre")

#Task 3: Light Show Technician Loop

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for x in range(len(genres)):
    genre = genres[x]
    if genre == 'Classical':
        break
    print("You are listening to track #",x, genre, "genre")