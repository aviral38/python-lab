number1=[1,2,3,4,5,6]
number2=[4,6,12,3,2,1]
add=list(map(lambda x,y:x+y,number1,number2))
print(add)
number3=[4,2,8,3,2,1]
mul=list(map(lambda x,y:x*y,number3,add))
print(mul)
