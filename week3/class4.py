x=int(input())
n=[]
d=[]
for i in range (x):
    y=int(input())
    z=int(input())
    n.append(y)
    d.append(z)
for i in range (x):
    p=1*n[i]
    q=1*d[i]
if p>=q:
    m=p
else:
    m=q
for i in range (1,q+1):
    if p%i==0 and q%i==0:
        p=p/i
        q=q/i
p=int(p)
q=int(q)
print("{} {}".format(p,q))
