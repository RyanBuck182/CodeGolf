import random as r;p=print;i=input
c="rock|paper|scissors|snake|bread|bowling ball|river|tomato|Computer |chose ".split("|")
l=lambda x,y,z:[c[x],c[y],c[z]]
a={c[0]:l(2,7,5),c[1]:l(0,5,4),c[2]:l(1,3,4),c[3]:l(1,4,6),c[4]:l(0,7,6),c[5]:l(3,7,2),c[6]:l(0,1,5),c[7]:l(2,3,6)}
while 1:
 p(f"Welcome to EXTREME {" ".join(c[:3])}!")
 for j in range(8):p(f" ({j+1}) {c[j]}")
 f=int(i("Your choice: "))
 if 0<f<9:u=c[f-1];break
 i("Invalid choice! Press enter to try again...")
p(f"You {c[9]+u}.")
m=r.choice(c[:8])
p(f"{c[8]+c[9]+m}.\n"+[["Tie! No one wins!",f"{c[8]}wins!"][u in a[m]],"You win!"][m in a[u]])