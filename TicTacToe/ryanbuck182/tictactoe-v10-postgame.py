import os;p=print;d="\n--+---+--\n";D=" | ".join;u=0;b=[*"123456789"];l=lambda x,y,z=1:{*b[x:y:z]}=={u}
while 1:
	p(D(b[:3])+d+D(b[3:6])+d+D(b[6:]))
	if l(0,3)|l(3,6)|l(6,9)|l(0,9,3)|l(1,9,3)|l(2,9,3)|l(0,9,4)|l(2,9,2):break
	elif len({*b})<3:u=0;break
	u='xo'[u=='x'];m=0
	while 1:
		m=input(u+" Pick a move (1-9): ")
		if m.isdigit()&(m in b):break
		p("Invalid move!")
	b[int(m)-1]=u;os.system('cls')
p([f"{u} wins!","It's a draw!"][u==0])