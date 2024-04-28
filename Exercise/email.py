answer=input('Do you already have email account').lower()
if answer=="no":
    email=input('Enter you email adress')
    if("@" in email) and email[-9:-4]=="gmail" or email[-9:-4]== "yahoo" in email:
      if email[-4:]==".com":
            password=input('Enter password (There must be at least 7 letter and digit)')
            if (len(password))>=7 and  password.isalnum() and (not password.isalpha()) and (not password.isdigit()):
                re_enter=input('Re-enter password')
                if password==re_enter:
                    print("your email account is created")
                else:
                    print('There is not your password')
            else:
                print("There must be at letter 7 latter and digit")
      else:
          print("please enter the '.com'")
    else:
        print("try again")
elif answer== "yes":
      email=input('Enter you email adress')
      if ("@" in email) and ("gmail" in email or "yahoo" in email) and (".com" in email):
        input('Enter password')
      else:
          print("some error in your email address")
else:
    print("try again")
