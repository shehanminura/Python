#Enter imadecl number : 20.456
#There are 3 decimal.
#Use len(number) & string.find
string=input("Enter decimal number:")
position=string.find(".")
if position != -1:
    if (string.count("."))==1:
        if string[:position].isdigit() and string[position+1:].isdigit() :
            decimal=((len(string))-position)-1
            print(f' There are {decimal} decimals')
        else:
            print("please enter only digit")
    else:
        print("invalid number")
else:
    print("please enter the '.'  ")










