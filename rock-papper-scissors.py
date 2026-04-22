import random

# function definitions
def rand_choice():
    return random.choice(["rock", "paper", "scissors"])

def normalize_choice(s):
    s = s.lower()
    if s.startswith("r"):
        return "rock"
    elif s.startswith("p"):
        return "paper"
    elif s.startswith("s"):
        return "scissors"
    else:
        return None

def does_computer_win(computer_choice, user_choice):
    if computer_choice == "rock" and user_choice == "scissors":
        return True
    if computer_choice == "paper" and user_choice == "rock":
        return True
    if computer_choice == "scissors" and user_choice == "paper":
        return True
    return False

def print_result(computer_choice, user_choice):
    if user_choice == computer_choice:
        print("Draw! The computer chose", computer_choice)
    elif does_computer_win(computer_choice, user_choice):
        print("You lose. The computer chose", computer_choice)
    else:
        print("You win! The computer chose", computer_choice)

# program begin
for i in range(3):
    computer_choice = rand_choice()
    
    user_input = input("Rock, paper or scissors? ")
    user_choice = normalize_choice(user_input)
    if user_choice is None:
        print("Invalid input.")
    else:
        print_result(computer_choice, user_choice)
# program end
