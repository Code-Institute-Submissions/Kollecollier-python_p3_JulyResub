#-----------------
def start_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)


questions = {
    "What is RAM short for?: ": "A",
    "What is CPU short for?: ": "B",
    "What is GPU short for?: ": "C",
    "What is SSD short for? : ": "A"
}

options = [["A. Random access memory", "B. Random access motor", "C. Racer access memory"],
           ["A. Core processor unit", "B. Central processor unit", "C, Core pro unit"],
           ["A. Great processor unit", "B. Graphics processor unit", "C. Graphic processor unit"],
           ["A. Solid State Drive", "B. Super State Drive", "C. Solid Super Drive"]]

start_game()