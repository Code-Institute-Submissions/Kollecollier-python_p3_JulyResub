def wrong():
    print("-----------------------")
    print("Sorry that was incorrect!")
    print("-----------------------")
    play = input("Try again?\n")
    if play == 'yes':
        print("-----------------------")
        print("Okej you've got this! 😉")
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
    print("Okej! Let's play!")
    print("-----------------------")
    start_quiz()


def start_quiz():
    print("First question! ")
    print("-----------------------")
    play = input("What is RAM short for?\n").lower()
    if play == "random access memory":
        print("-----------------------")
        print("That's correct! Well done 😊")
        print("-----------------------")
        correct_answer()
    else:
        wrong()


def restart_quiz():
    print("Let's try again")
    start_quiz()


def correct_answer():
    play = input('Okej next question, What is GPU short for?\n').lower()
    if play == "graphics processing unit":
        print("-----------------------")
        print("Correct, Good job! 😊 ")
        print("-----------------------")
        print("Now let's move on to the next question!")
        print("-----------------------")
        play = input("What is SSD short for?\n").lower()
        if play == 'Solid State Drive':
            print("-----------------------")
            print('That is correct! 😊')
            print("-----------------------")
    else:
        wrong()


ask_to_play()
wrong()