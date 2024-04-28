
while(True):
    x=0
    z = 10
    while x<10:
        x+=1
        z-=1
        print(" "*z,"x "*x)

    while z<10:
        x -= 1
        z += 1
        print(" "*z,"x "*x)
    break