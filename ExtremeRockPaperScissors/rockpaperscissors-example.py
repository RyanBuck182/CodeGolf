import random

choices = ["rock", "paper", "scissors", "snake", "bread", "bowling ball", "river", "tomato"]

wins_against = {
    "rock":         ["scissors", "tomato", "bowling ball"],
    "paper":        ["rock", "bowling ball", "bread"],
    "scissors":     ["paper", "snake", "bread"],
    "snake":        ["paper", "bread", "river"],
    "bread":        ["rock", "tomato", "river"],
    "bowling ball": ["snake", "tomato", "scissors"],
    "river":        ["rock", "paper", "bowling ball"],
    "tomato":       ["scissors", "snake", "river"],
}


def get_user_choice():
    print("Welcome to EXTREME rock paper scissors!")
    print(" (1) rock")
    print(" (2) paper")
    print(" (3) scissors")
    print(" (4) snake")
    print(" (5) bread")
    print(" (6) bowling ball")
    print(" (7) river")
    print(" (8) tomato")
    choice = int(input("Your choice: "))
    return choices[choice - 1]


def main():
    while True:
        user_choice = get_user_choice()
        if user_choice in choices:
            break
        input("Invalid choice! Press enter to try again...")
    print(f"You chose {user_choice}.")

    cpu_choice = random.choice(choices)
    print(f"Computer chose {cpu_choice}.")

    if cpu_choice in wins_against[user_choice]:
        print("You win!")
    elif user_choice in wins_against[cpu_choice]:
        print("Computer wins!")
    else:
        print("Tie! No one wins!")


if __name__ == "__main__":
    main()
