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



