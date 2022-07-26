import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_project_sheet')
score_sheet = SHEET.worksheet('store_correct1')

questions = [
    {
        "question": "What is RAM short for?",
        "options": [
            "a) Random Memory",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Access Memory"
        ],
        "correct_answer": "c"
    },
    {
        "question": "What is GPU short for?",
        "options": [
            "a) Graphical Processing Unit",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Access Memory"
            ],
        "correct_answer": "a"
    },
    {
        "question": "What is SSD short for?",
        "options": [
            "a) Random Memory",
            "b) Solid State Drive",
            "c) Random Access Memory",
            "d) Access Memory"
            ],
        "correct_answer": "b"
    },
    {
        "question": "What is PSU short for?",
        "options": [
            "a) Random Memory",
            "b) Random Access",
            "c) Random Access Memory",
            "d) Power Supply Unit"
            ],
        "correct_answer": "d"
    }
]


def ask_to_play():
    """
    This function defines the start of the game
    """
    print('Welcome to my computer quiz!\n')
    play = input('Do you want to play? Yes or No ?\n').lower()
    if play == "":
        print("Invalid input, try again!\n")
        return ask_to_play()
    elif play == 'no':
        print('Thank you!')
        return
    else:
        return start_game()


def start_game():
    """
    Giving the user a feedback comment and also engageing the quiz
    """
    user_name = input("\nPlease enter your name:\n")
    if user_name == "":
        print("Invalid input, Try again")
        return start_game()
    else:
        print("Okej! Let's Go!\n")
        return start_quiz(user_name)


def update_score_to_sheet(score, user_name):
    """
    This funtion is coded to provide scores to the googlesheet
    """
    no_of_rows = len(score_sheet.col_values(1))
    score_sheet.update_cell(no_of_rows+1, 1, user_name)
    score_sheet.update_cell(no_of_rows+1, 2, score)


def start_quiz(user_name):
    """
    Here the quiz begins after all the correct user inputs
    """
    score = 0
    for question in questions:
        print(question["question"])
        question_options = question["options"]
        for option in question_options:
            print(option)
        user_choice = get_option_input()
        if user_choice == question["correct_answer"]:
            score += 1
            print("-----------------\nCorrect! Well done!\n----------------")
        else:
            print("Incorrect Input\n")
    update_score_to_sheet(score, user_name)
    end_game()


def get_option_input():
    user_input = input('\nEnter either a/b/c/d:\n').lower()
    if user_input == "" or user_input not in ["a", "b", "c", "d"]:
        print("Incorrect Input\nPlease enter again\n")
        return get_option_input()
    return user_input


def end_game():
    """
    This ends the game and provides user a thank you and some information
    """
    print("Thank you for playing my first python quiz game\n")
    print("Your score has been added to the scoreboard\n")
    print("You can find the scoreboard in the README.md file!")


ask_to_play()
