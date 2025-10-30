import random
i=input
P=print
r="rock"
p="paper"
v="scissors"
s="snake"
b="bread"
B="bowling ball"
R="river"
t="tomato"
c=[r,p,v,s,b,B,R,t]
w={r:[v,t,B],p:[r,B,b],v:[p,s,b],s:[p,b,R],b:[r,t,R],B:[s,t,v],R:[r,p,B],t:[v,s,R]}
while 1:
 u=i(f"Welcome to EXTREME {r} {p} {v}!\n (1) {r}\n (2) {p}\n (3) {v}\n (4) {s}\n (5) {b}\n (6) {B}\n (7) {R}\n (8) {t}\nYour choice: ")
 if u in"12345678":break
 i("Invalid choice! Press enter to try again...")
u=c[int(u)-1]
P(f"You chose {u}.")
m=random.choice(c)
P(f"Computer chose {m}.")
P("You win!"if m in w[u]else"Computer wins!"if m in w[m]else"Tie! No one wins!")