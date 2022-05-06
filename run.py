print("Welcome to my computer quiz!")

play = input('Do you want to play? ')
"""
Welcome messege ans also asking if the user wishes to particiapte in the game.
"""

if play.lower() != 'yes':
    quit()

print("Okej, Let's play, Select your answer by entering: a, b, or c.")
"""
The if statment determinates if the user want's to play ! If other than yes, game will quit!
"""

answer = input("What is 'RAM' short for? a: Random access memory. b: Raid access memory. c: Running access memory? ")

if answer.lower() == "a" :
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What dose 'GPU' stand for? a: graphic processor unit. b: graphics processing unit  c: graphiccard processor unit ")

if answer.lower() == "b" :
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Wha dose CPU stand for? a: central progess unit. b: central processor unit. c: central processing unit. ")

if answer.lower() == "c" :
    print("Correct!")
else:
    print("Incorrect!")
