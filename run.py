def ask_to_play():
    print('Welcome to my computer quiz')
    play = input('Do you want to play? ')
    if play == "yes":
        start_game()
    else:
        print("To bad maybe next time?")
        exit()


def start_game():
    print("Okej! Let's play!")
    start_quiz()


def start_quiz():
    print("First question! ")
    print("-----------------------")
    playing = input ("What is RAM short for?\n")
    if playing == "central processing unit":
        print("That's correct! Well done 😊")
    else:
        print("Incorrect, try again?")
        play = input("yes or no? ")
        if play == 'yes':
            print("----------")
            restart_quiz()
            print("-------------")    


def restart_quiz():
    print("Let's try again")
    start_quiz()


ask_to_play()