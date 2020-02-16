def cube(x):
    return x*x*x
cube1=list(map(cube,[1,2,3]))
print(cube1)
#using lambda
cube2=list(map(lambda x:x*x*x,[1,2,3]))
print(cube2)
