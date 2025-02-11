import os;p=print;n="\n";d=n+"--+---+--"+n;D=" | ".join;u=0;b=list(map(str,[1,2,3,4,5,6,7,8,9]));l=lambda x,y,z=1:b[x:y:z].count(b[x])==3
while 1:
	p(D(b[:3])+d+D(b[3:6])+d+D(b[6:]))
	if l(0,3)or l(3,6)or l(6,9)or l(0,9,3)or l(1,9,3)or l(2,9,3)or l(0,9,4)or l(2,9,2):break
	elif {*b}=={'x','o'}:u='d';break
	u='o'if u=='x'else'x';m=0
	while 1:
		m=input(u+" Pick a move (1-9): ")
		if m.isnumeric()and m in b:break
		else:p("Invalid move!")
	b[int(m)-1]=u;os.system('cls')
p("It's a draw!")if u=='d'else p(u+" wins!")