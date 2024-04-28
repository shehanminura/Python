#find the given number whether  divides by 2 and 3
marke=12
if marke % 2==0:
    if marke % 3==0:
         print(f'number{marke} divides by 3&2')
    else:
       print(f'numbr{marke} divides by only 2')

else:
    if marke % 3==0:
        print(f'number{marke}divides by only 3')
    else:
        print(f'number{marke} not divides by 2&3')
