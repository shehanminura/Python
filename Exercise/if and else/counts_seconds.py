#Time : 12: 55 :34
# a.m or p.m ? am
#______ seconds are over in this day
time=input("Enter time")
what_time=input("Enter am or pm")
if time.count(":")==2:
   find_col1=time.find(":")
   find_col2=time.find(":",find_col1+1)

   hour1=time[:find_col1]
   min1=time[find_col1+1:find_col2]
   second1=time[find_col2:]

   if (time[:find_col1]).isdigit() and (time[find_col1+1:find_col2]).isdigit() and (time[find_col2+1:]).isdigit():
      if int(time[:find_col1])<13 and int(time[find_col1+1:find_col2])<60 and int(time[find_col2+1:])<60:
        if what_time=="am":
            hour=int(time[:find_col1])*3600
            min=int(time[find_col1+1:find_col2])*60
            seconds=int(time[find_col2+1:])*1
            All_seconds=(hour+min+seconds)
            print(f'{All_seconds} seconds are over this day')
            if len(hour1)==1:
              hour1="0"+hour1
            if len(min1)==1:
                min1="0"+min1
            print(f'{hour1}{min1}h')
        elif what_time=="pm":
            hour=(int(time[:find_col1])+12)*3600
            min=int(time[find_col1+1:find_col2])*60
            seconds=int(time[find_col2+1:])*1
            All_seconds=(hour+min+seconds)
            print(f'{All_seconds} seconds are over this day')
            z=int(time[:find_col1])+12
            print(f'{z}{(time[find_col1+1:find_col2])}h')

        else:
            print("please enter the am or pm ")
      else:
          print("try again")
   else:
        print("try again")