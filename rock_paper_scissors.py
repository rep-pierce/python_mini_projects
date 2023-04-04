import random

user_wins = 0
computer_wins = 0
computer_states = {1: "rock", 2: "paper", 3: "scissors"}


while True:
    user_input = input("Type Rock/Paper/Scissors or q to quit: ")
    computer_throw = computer_states[random.randint(1, 3)]
    if user_input.lower() == "q":
        print(f"Total Scores: User Wins = {user_wins} | Computer Wins = {computer_wins}")
        quit()

    if user_input.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid input, try again")
        continue

    if computer_throw == user_input.lower():
        print(f"Computer threw {computer_throw}")
        print("Tie")
        continue
    elif computer_throw == "rock":
        if user_input.lower() == "paper":
            print(f"Computer threw {computer_throw}, you win")
            user_wins += 1
        else:
            print(f"Computer threw {computer_throw}, computer wins")
            computer_wins += 1
    elif computer_throw == "paper":
        if user_input.lower() == "rock":
            print(f"Computer threw {computer_throw}, you win")
            user_wins += 1
        else:
            print(f"Computer threw {computer_throw}, computer wins")
            computer_wins += 1
    else:
        if user_input.lower() == "rock":
            print(f"Computer threw {computer_throw}, you win")
            user_wins += 1
        else:
            print(f"Computer threw {computer_throw}, computer wins")
            computer_wins += 1
    
    print(f"You have {user_wins} wins, Computer has {computer_wins} wins")

