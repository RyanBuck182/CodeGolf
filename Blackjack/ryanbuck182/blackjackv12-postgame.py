import random as r;p=print;w=input;l=list;e=exit;u=21;s=11;a="Spades|Hearts|Diamonds|Clubs|Jack|Queen|King|Ace|Tie!\n|busted!|Dealer wins!\n|You win!\n".split('|');R=l("23456789")+a[4:8];d=[(i,R[i],q,int((R[:8]+[10]*3+[s])[i]))for q in a[:4]for i in range(12)];k=lambda:d.pop();r.shuffle(d);h=[k(),k()];b=[k(),k()]
def x(z):
 n=m=0
 for c in z:n+=c[3];m+=c[0]==s
 while(n>u)*m>0:m-=1;n-=10
 return n
def y(h):
 for c in h:p(" ",c[1],"of",c[2])
def t(n=1):
 p();m="Dealer's Hand ("
 if n:p(m+f"{x(b)}):");y(b)
 else:p(m+"?):\n  ???");y(b[1:])
 p(f"Your Hand ({x(h)}):");y(h)
def g(z):t();p(a[z])
if(x(b)==u)*x(h)==u:g(8);e()
elif x(b)==u:g(10);e()
elif x(h)==u:g(s);e()
t(0)
while x(h)<u:
 c=w("Hit or stand? (h/s): ")
 if c in'sS':break
 if c in'hH':h+=[k()];t(0)
 else:p("ERROR: Invalid input!")
if x(h)==u:p(a[s]);e()
if x(h)>u:p("You",*a[9:s]);e()
while x(b)<17:t();b+=[k()];w("Press enter to continue...")
if x(b)>u:t();p("Dealer",*a[9::2])
elif x(h)>x(b):g(s)
elif x(b)>x(h):g(10)
else:g(8)