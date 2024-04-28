#palindrome number : 131,141,27827,4567654
#find all palindrome numbers betwen 100 and 10000 and count it
number=100
count=0
while (number<10000):                                 #while (number<10000)
     number = number + 1                                    #number+=1
     if str(number) == str(number)[::-1] :                  #value=str(number)
         count+=1                                           #if vlue=vlue[::-1]
         print(number)                                          #print(vlue)
         print(count)

