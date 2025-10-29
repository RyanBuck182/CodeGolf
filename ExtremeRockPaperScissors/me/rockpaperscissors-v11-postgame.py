import random as r;p=print;i=input;k=int
c="rock|paper|scissors|snake|bread|bowling ball|river|tomato|Computer |chose ".split("|")
l=lambda x,y,z:[c[k(x)],c[k(y)],c[k(z)]]
s="0275|1054|2134|3146|4076|5372|6015|7236"
a={c[k(w)]:l(x,y,z)for w,x,y,z in s.split("|")}
while 1:
 p(f"Welcome to EXTREME {" ".join(c[:3])}!")
 for j in range(8):p(f" ({j+1}) {c[j]}")
 f=k(i("Your choice: "))
 if 0<f<9:u=c[f-1];break
 i("Invalid choice! Press enter to try again...")
p(f"You {c[9]+u}.")
m=r.choice(c[:8])
p(f"{c[8]+c[9]+m}.\n"+[["Tie! No one wins!",f"{c[8]}wins!"][u in a[m]],"You win!"][m in a[u]])