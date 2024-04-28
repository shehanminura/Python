#enter the number:7
#7 is prime number
#enter the number:9
#9 is not a prime number
number1=input("Enter number")
number=int(number1)
i=2
while(i<number):
    if number%i==0 :
        print(f'{number} is not prime number')
        break
    if i==number-1:
           print(f'{number} is prime number')
    i+=1

