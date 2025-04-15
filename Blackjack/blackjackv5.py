import random as r
p=print
w=input
l=list
e=exit
a="Spades|Hearts|Diamonds|Clubs|Jack|Queen|King|Ace|Tie!\n|Dealer wins!\n|You win!\n".split('|')
R=l("23456789")+a[4:8]
def x(z):
    n=0;m=0
    for c in z:n+=c[3];m+=1 if c[0]==11 else 0
    while n>21 and m>0:m-=1;n-=10
    return n
def y(h):
    for c in h:p(f"  {c[1]} of {c[2]}")
def t(h,z,n=0):
    p()
    m="Dealer's Hand ("
    if n:p(m+f"{x(z)}):");y(z)
    else:p(m+"?):");p("  ???");y(z[1:])
    p(f"Your Hand ({x(h)}):");y(h)
d=[(i,v,q,l(map(int,R[:8]+[10]*3+[11]))[i]) for q in a[:4]for i,v in enumerate(R)]
r.shuffle(d)
h=[d.pop(),d.pop()]
b=[d.pop(),d.pop()]
if x(b)==21 and x(h)==21:t(h,b,n=1);p(a[8]);e()
elif x(b)==21:t(h,b,n=1);p(a[9]);e()
elif x(h)==21:t(h,b,n=1);p(a[10]);e()
t(h,b)
while x(h)<21:
    choice=w("Hit or stand? (h/s): ").lower()
    if choice=='h':h.append(d.pop());t(h,b)
    elif choice=='s':break
    else:p("ERROR: Invalid input!")
if x(h)==21:p(a[10]);e()
if x(h)>21:p("You busted! Dealer wins!\n");e()
while x(b)<17:t(h,b,n=1);b.append(d.pop());w("Press enter to continue...")
if x(b)>21:t(h,b,n=1);p("Dealer busted! You win!\n")
elif x(h)>x(b):t(h,b,n=1);p("You win!\n")
elif x(b)>x(h):t(h,b,n=1);p(a[9])
else:t(h,b,n=1);p(a[8])