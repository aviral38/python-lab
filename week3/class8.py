def leap(z):
    if z%4==0:
        if z%100==0:
            if z%400==0:
                print("leap year")
            else:
                print("NOt leap")
        else:
            print("leap year")
    else:
        print("not leap")
y=int(input())
leap(y)
