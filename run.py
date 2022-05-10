questions = [
    {
        "question": "What is 'RAM' short for? a: Random access memory. b: Raid access memory. c: Running access memory?",
        "correct_answer": "a"
    },
    {
        "question": "What is CPU short for? a: Central progess unit. b: Central processor unit. c: Central processing unit. ",
        "correct_answer": "b"
    },
    {
        "question": "What is 'RAM' short for? a: Random access memory. b: Raid access memory. c: Running access memory?",
        "correct_answer": "a"
    },
    {
        "question": "What is 'RAM' short for? a: Random access memory. b: Raid access memory. c: Running access memory?",
        "correct_answer": "a"
    },
    {
        "question": "What is 'RAM' short for? a: Random access memory. b: Raid access memory. c: Running access memory?",
        "correct_answer": "a"
    }
]




# play = input('Do you want to play? ')
# """
# Welcome messege ans also asking if the user wishes to particiapte in the game.
# """
# if play.lower() != 'yes':
#     quit()
# print("Okej, Let's play, Select your answer by entering: a, b, or c.")
# score = 0
# """
# The if statment determinates if the user want's to play !
# """

#     print("Incorrect!")
# answer = input("What is 'GPU' short for? a: Graphic processor unit. b: Graphics processing unit  c: Graphic card processor unit ")
# if answer.lower() == "b":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")
# answer = input("What is CPU short for? a: Central progess unit. b: Central processor unit. c: Central processing unit. ")
# if answer.lower() == "c":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")
# answer = input("What is SSD short for? a: Solid state drive. b: Super state drive. c:Super speed drive. ")
# if answer.lower() == "a":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect!")
# print("You got " + str(score) + " questions right! Well done!")


def start_quiz():
    #Loop through the questions and ask user the answers
    for question in questions:
        print(question['question'])
        user_ans_input = input("")
        if user_ans_input == question['correct_answer']:
            #Increment score
        else:
            #print some message
    #Display final score here


def ask_to_play():
    play = input('Do you want to play? Press Y for yes or press anything to exit')
    if play == 'Y':
        start_quiz()
    else:
        #Exit the game by displaying message

def start_game():
    print("Welcome to my computer quiz!")
    ask_to_play()


start_game()