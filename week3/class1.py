import math
a=int(input())
b=int(input())
c=int(input())
dd=int(input())
s=[]
su=[]
m=[]
d=[]
mo=[]
moo=[]
k=float(a+c)
s.append(k)
k=float(b+dd)
s.append(k)
k=float(a-c)
su.append(k)
k=float(b-dd)
su.append(k)
k=float((a*c)-(b*dd))
m.append(k)
k=float((b*c)+(a*dd))
m.append(k)
e=(c*c)+dd*dd
dd=-dd
k=float(((a*c)-(b*dd))/e)
d.append(k)
k=float(((b*c)+(a*dd))/e)
d.append(k)
k=float(math.sqrt((a*a)+(b*b)))
mo.append(k)
mo.append(0.00)
k=float(math.sqrt((c*c)+(dd*dd)))
moo.append(k)
moo.append(0.00)
print("{:0.2f}{:+0.2f}i".format(s[0],s[1]))
print("{:0.2f}{:+0.2f}i".format(su[0],su[1]))
print("{:0.2f}{:+0.2f}i".format(m[0],m[1]))
print("{:0.2f}{:+0.2f}i".format(d[0],d[1]))
print("{:0.2f}{:+0.2}i".format(mo[0],mo[1]))
print("{:0.2f}{:+0.2}i".format(moo[0],moo[1]))
