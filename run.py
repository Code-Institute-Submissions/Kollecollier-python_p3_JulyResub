questions = {
    "1": "What is RAM short for?",
    "2": "What is GPU short for?",
    "3": "What is SSD short for?",
    "4": "What is PSU short for?"
}


def wrong():
    print("-----------\nSorry that was incorrect😞!\n-----------")
    play = input("Try again?\n")
    if play == 'yes':
        print("-----------------\nOkej you've got this😉!\n-----------------")
        print("Let's try again!\n-----------------")
        start_quiz()
    else:
        print("To bad maybe next time?")
        exit()


def ask_to_play():
    print('Welcome to my computer quiz!\n')
    play = input('Do you want to play? Yes or No ?\n').lower()
    if play == "yes":
        start_game()
    else:
        print("To bad maybe next time?")
        exit()


def start_game():
    """
    Giving the user a feedback comment and also engageing the quiz
    """
    print("-----------------\nOkej! Let's play 😊!\n-----------------")
    start_quiz()


def start_quiz():
    print("First question!\n-----------------")
    print(questions["1"])
    play = input('').lower()
    if play == "random access memory":
        print("-----------------\nCorrect! Well done😊!!\n-----------------")
        question_2()
    else:
        wrong()


def restart_quiz():
    print("Let's try again")
    start_quiz()


def question_2():
    print('Okej next question\n-----------------')
    print(questions["2"])
    play = input('').lower()
    if play == "graphics processing unit":
        print("-----------------\nCorrect! Well done😊!\n-----------------")
        print("Now on to the next question!\n-----------------")
        question_3()
    else:
        wrong()


def question_3():
    print(questions["3"])
    play = input("").lower()
    if play == "solid state drive":
        print("-----------------\nCorrect! You're a pro😁!\n-----------------")
        last_question()
    else:
        wrong()


def last_question():
    print("Well done, you made it to the final round☠️\n-----------------")
    print(questions["4"])
    play = input("").lower()
    if play == "power supply unit":
        print("-----------------\nCongratz! You are a pro!\n-----------------")


def end_game():
    print("Thank you for playing my first python quiz game")


ask_to_play()