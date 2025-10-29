import random as r
p=print
i=input
c="rock|paper|scissors|snake|bread|bowling ball|river|tomato|Computer |chose ".split("|")
a={c[0]:[c[2],c[7],c[5]],c[1]:[c[0],c[5],c[4]],c[2]:[c[1],c[3],c[4]],c[3]:[c[1],c[4],c[6]],c[4]:[c[0],c[7],c[6]],c[5]:[c[3],c[7],c[2]],c[6]:[c[0],c[1],c[5]],c[7]:[c[2],c[3],c[6]],}
while 1:
 p("Welcome to EXTREME rock paper scissors!")
 for j in range(8):p(f" ({j+1}) {c[j]}")
 f=int(i("Your choice: "))
 if 0<f<9:u=c[f-1];break
 i("Invalid choice! Press enter to try again...")
p(f"You {c[9]+u}.")
m=r.choice(c[:8])
p(f"{c[8]+c[9]+m}.")
if m in a[u]:p("You win!")
elif u in a[m]:p("Computer wins!")
else:p("Tie! No one wins!")