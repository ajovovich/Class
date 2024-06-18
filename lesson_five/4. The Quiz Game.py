questions = [
"What does the color blue and green combine to make?" , 
"What is 2+2" , 
"Is a square four equal sides?" ,
"What is the first 3 digits of Pi?"
]



def quiz(questions, score):
    correct_answers = ["yellow", 4, True, 3.14]
    answer_types = [str, int, bool, float]

    for i in range(len(questions)):
        user_answer = input(questions[i] + '').lower()
        try:
            if answer_types[i] == bool:
                converted_answer = user_answer.lower() in ['true', 't', 'yes', 'y']
            else:
                converted_answer = answer_types[i](user_answer)

            if converted_answer == correct_answers[i]:
                print("Correct!")
                score += 1
            else:
                print('Incorrect!')
        except ValueError:
            print("Invalid input")
    return score

score = 0          
user_quiz = quiz(questions, score)
if user_quiz == 4:
    print("Amazing job, you received 100% on your quiz")

elif user_quiz == 3:
    print("Good work, you received 75% on your quiz")

elif user_quiz == 2:
    print("You received 50% on your quiz, review and try again!")

elif user_quiz == 1:
    print("You received 25% on your quiz, study and try again!")

else:
    print("You receieved 0%, dont try to guess, you got this!")