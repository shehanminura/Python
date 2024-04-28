#12.00.00
#12.00.01
#12.00.02

#12.00.59
#12.01.00
#12.01.01


#12.59.59
#13.00.00
h=12
while h<13 :
    min=0
    while min<60:
        sec = 0
        while sec<60:
                minutes=min
                second=sec
                if len(str(sec))!=2:
                    second='0'+str(sec)

                if len(str(min))!=2:
                    minutes = '0'+str(min)
                print(f'{h}:{minutes}:{second}')
                sec+=1
        min+=1
    h += 1
    min=0
    sec=0
    print(f"{h}:0{min}:0{sec}")
