name=input("Enter the Name")
if name.isalpha():
    x=len(name)-1
    y=name[:-1].lower()
    z=name.replace(name[x],name[x].upper())
    print(y + z[-1])
else:
    print("Please enter the name using characters")



