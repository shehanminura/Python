count = 0
while(True):

        answer=input("Do you love me").lower()
        if answer=="yes":
            print("Thank you")
            print(f"you {count} years later she gave word ")
            break
        if answer=="no":
            count += 1
            print("one year later")

