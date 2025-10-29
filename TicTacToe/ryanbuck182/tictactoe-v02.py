import os;p=print;n="\n";d=n+"--+---+--"+n;D=" | ".join;u=0;b=list(map(str,[1,2,3,4,5,6,7,8,9]))
while 1:
	p(D(b[:3])+d+D(b[3:6])+d+D(b[6:]))
	if b[0:3].count(b[0])==3:break
	elif b[3:6].count(b[3])==3:break
	elif b[6:9].count(b[3])==3:break
	elif b[0::3].count(b[0])==3:break
	elif b[1::3].count(b[1])==3:break
	elif b[2::3].count(b[2])==3:break
	elif b[0::4].count(b[0])==3:break
	elif b[2::2].count(b[2])==3:break
	elif {*b}=={'x','o'}: u='d';break
	u='o'if u=='x'else'x';m=''
	while 1:
		m=input(u+" Pick a move (1-9): ")
		if m.isnumeric()and m in b:break
		else:p("Invalid move!")
	b[int(m)-1]=u;os.system('cls')
p("It's a draw!")if u=='d'else p(u+" wins!")