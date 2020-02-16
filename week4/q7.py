num1=[1,2,3,4,5,6]
num2=[4,6,12,3,2,1]
num3=[]
add=list(map(lambda x,y:x+y,num1,num2))
print(add)
x=list(map(lambda x,y:x/y,num1,num2))
print(x)
y=list(map(lambda z:z%2,x))
print(y)
