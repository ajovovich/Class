#Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

#Task 2: Venue Selection

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
system = "You should use an audio system" if attendees > 100 else "You should use a projector"
print(venue,system)

#Task 3: Catering Choices

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
system = "You should use an audio system" if attendees > 100 else "You should use a projector"
print(venue,system)

catering = input("Select food option (Vegetarian/Regular)")

food_choice = "Veggie Delight Caterers" if catering == "Vegetarian" else "Gourment Meals Caterers"
print(food_choice)