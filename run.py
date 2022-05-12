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
    print("-----------------\nOkej! Let's play 😊!\n-----------------")
    start_quiz()


def start_quiz():
    print("First question!\n-----------------")
    play = input('What is RAM short for ?\n').lower()
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
    play = input('What is GPU short for?\n').lower()
    if play == "graphics processing unit":
        print("-----------------\nCorrect! Well done😊!\n-----------------")
        print("Now on to the next question!\n-----------------")
        question_3()
    else:
        wrong()


def question_3():
    play = input("What is SSD short for?\n").lower()
    if play == "solid state drive":
        print("-----------------\nCorrect! You're a pro😁!\n-----------------")
        last_question()
    else:
        wrong()


def last_question():
    print("Well done, you made it to the final round☠️\n-----------------")
    play = input("What is PSU short for?\n").lower()
    if play == "power supply unit":
        print("-----------------\nCongratz! You are a pro!\n-----------------")


def end_game():
    print("Thank you for playing my first python quiz game")


ask_to_play()