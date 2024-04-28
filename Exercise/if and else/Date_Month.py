print('Enter the number of  Month :',end='')
month=4
#if month
# 'this month has 31 days')
print('Enter the year:',end='')

year=2020
month=8
print(f"enter the year:{year}")
print(f'Enter the number of  Month :{month}')

if month<13:
 if month==2:
    if year % 4 ==0:
          print("this month has 29 day")
    else:
             print("this month has 28 day")
 elif month<8:
     if month % 2==0:
        print("this month has 30 day")
     else:
        print("this month has 31 day ")
 else:
     if month % 2 ==0:
         print("this month has 31 day ")
     else:
         print("this month has 30 day")
else:
    print("pleans enter only  since 1 to 12 ")




