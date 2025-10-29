import random as r
p=print
w=input
l=list
e=exit
u=21
a="Spades|Hearts|Diamonds|Clubs|Jack|Queen|King|Ace|Tie!\n|busted!|Dealer wins!\n|You win!\n".split('|')
R=l("23456789")+a[4:8]
def x(z):
    n=0;m=0
    for c in z:n+=c[3];m+=[0,1][c[0]==11]
    while (n>u)*m>0:m-=1;n-=10
    return n
def y(h):
    for c in h:p(f"  {c[1]} of {c[2]}")
def t(h,z,n=0):
    p();m="Dealer's Hand ("
    if n:p(m+f"{x(z)}):");y(z)
    else:p(m+"?):");p("  ???");y(z[1:])
    p(f"Your Hand ({x(h)}):");y(h)
d=[(i,v,q,l(map(int,R[:8]+[10]*3+[11]))[i]) for q in a[:4]for i,v in enumerate(R)]
r.shuffle(d)
k=lambda:d.pop()
h=[k(),k()]
b=[k(),k()]
s=lambda:t(h,b,1)
def g(z):s();p(a[z])
if x(b)==u and x(h)==u:g(8);e()
elif x(b)==u:g(10);e()
elif x(h)==u:g(11);e()
t(h,b)
while x(h)<u:
    c=w("Hit or stand? (h/s): ").lower()
    if c=='h':h+=[k()];t(h,b)
    elif c=='s':break
    else:p("ERROR: Invalid input!")
if x(h)==u:p(a[11]);e()
if x(h)>u:p("You",*a[9:11]);e()
while x(b)<17:s();b+=[k()];w("Press enter to continue...")
if x(b)>u:s();p("Dealer",*a[9::2])
elif x(h)>x(b):g(11)
elif x(b)>x(h):g(10)
else:g(8)