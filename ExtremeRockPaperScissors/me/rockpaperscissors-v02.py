import random
p=print
i=input
choices=["rock","paper","scissors","snake","bread","bowling ball","river","tomato"]
wins_against={"rock":["scissors","tomato","bowling ball"],"paper":["rock","bowling ball","bread"],"scissors":["paper","snake","bread"],"snake":["paper","bread","river"],"bread":["rock","tomato","river"],"bowling ball":["snake","tomato","scissors"],"river":["rock","paper","bowling ball"],"tomato":["scissors","snake","river"],}
def get_user_choice():
    p("Welcome to EXTREME rock paper scissors!")
    p(" (1) rock")
    p(" (2) paper")
    p(" (3) scissors")
    p(" (4) snake")
    p(" (5) bread")
    p(" (6) bowling ball")
    p(" (7) river")
    p(" (8) tomato")
    choice = int(i("Your choice: "))
    return choices[choice - 1]
def main():
    while True:
        user_choice = get_user_choice()
        if user_choice in choices:
            break
        i("Invalid choice! Press enter to try again...")
    p(f"You chose {user_choice}.")

    cpu_choice = random.choice(choices)
    p(f"Computer chose {cpu_choice}.")

    if cpu_choice in wins_against[user_choice]:
        p("You win!")
    elif user_choice in wins_against[cpu_choice]:
        p("Computer wins!")
    else:
        p("Tie! No one wins!")
if __name__ == "__main__":
    main()