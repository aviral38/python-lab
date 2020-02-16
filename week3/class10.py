l=[]
for i in range (5):
    x=int(input())
    l.append(x)
l.sort()
max=0
min=0
for i in range (1,5):
    max=max+l[i]
for i in range (4):
    min=min+l[i]
print("{} {}".format(min,max))
