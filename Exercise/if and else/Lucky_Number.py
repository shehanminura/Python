#Enter your Birth Date: 1895/06/22
#enter Lucky Number is : 7
#calculation part: 1+8+9+5+0+6+2+2=43
#then 4+3=7
#you can use replase method
#use while
#lucky_number+=[variyable]

lucky_number = 0
birth_day=input("Enter your Birth Date")
slash1=birth_day.find("/")
slash2=birth_day.find('/',slash1+1)
if birth_day[4]=="/" and birth_day[6]=="/" or birth_day[7]=="/":
    if birth_day[:slash1].isdigit() and birth_day[slash1+1:slash2].isdigit() and birth_day[slash2+1:]:
        number = birth_day.replace("/", "")
        while number:
            lucky_number += int(number[0])
            number = number[1:]
        lucky =str(lucky_number)[:2]
        if int(lucky)<10:
            print(f'Your Lucky Number is: {lucky}')
        else:
            lucky=int(lucky[0])+int(lucky[1])
            print(f'Your Lucky Number is: {lucky}')


date=input("Enter the date of birth")
if(date.count("/")==2):
    date=date.replace("/","")
    if(date.isdigit()):
        while(True):
                index=0
                #print("abc",date)
                lucky_number = 0
                while (index<len(date)):
                    #print( index, date)
                    lucky_number+=int(date[index])
                    index+=1
                if len(str(lucky_number))==1:
                    print(lucky_number)
                    break
                else:
                   date=str(lucky_number)
                   #print('date',date)
                   #print("in",lucky_number)



