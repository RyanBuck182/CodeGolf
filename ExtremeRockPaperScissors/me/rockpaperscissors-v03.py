import random as r
p=print
i=input
c=["rock","paper","scissors","snake","bread","bowling ball","river","tomato"]
a={c[0]:[c[2],c[7],c[5]],c[1]:[c[0],c[5],c[4]],c[2]:[c[1],c[3],c[4]],c[3]:[c[1],c[4],c[6]],c[4]:[c[0],c[7],c[6]],c[5]:[c[3],c[7],c[2]],c[6]:[c[0],c[1],c[5]],c[7]:[c[2],c[3],c[6]],}
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
    choice=int(i("Your choice: "))
    return c[choice - 1]
def main():
    while 1:
        user_choice=get_user_choice()
        if user_choice in c:
            break
        i("Invalid choice! Press enter to try again...")
    p(f"You chose {user_choice}.")

    cpu_choice = r.choice(c)
    p(f"Computer chose {cpu_choice}.")

    if cpu_choice in a[user_choice]:
        p("You win!")
    elif user_choice in a[cpu_choice]:
        p("Computer wins!")
    else:
        p("Tie! No one wins!")
if __name__=="__main__":main()