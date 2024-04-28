#print only 5 time number below than 100

number=0
while(True):
    number+=5
    if(number==100):
        break
    if (number%5!=0):
        continue
    print(number)


#when theacher enter the marke
#you want to creat a program to print out only then 50 marks
#when teacher finished, she will enter -1
#Enter the marks :60



while(True):
    marks=input("enter the marks:")   #marke=int(input("zxdchgf")
    if marks.isdigit():
        marks=int(marks)     # pallahayin da marks int kara atha
    else:
        print("Invalid")
    if(int(marks)==-1):
        break
    if(int(marks)<50):
        continue
    print(f"{marks} marke is enter")