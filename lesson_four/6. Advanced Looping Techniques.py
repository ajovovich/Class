# Task 1: The Selective DJ
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sub_genres = []
for x in range(len(genres)):
    genre = genres[x]
    sub_genres = genres[1:4] #Cut out Jazz from the genre list
    print("You are listening to track #",x, sub_genres, "genre")

# Task 2: The One-Liner Band with List Comprehensions

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
new_genres = []
for item in genres:
    new_genres.append(item + ' Music' [:10])
        
print(new_genres)

#Task 3: Numerical Beats with range


for i in range(10, 0, -1):
    print(i)
    if i == 1:
        print("The beat has dropped!")