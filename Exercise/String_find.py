
date = input("Enter Your birth date :(yyyy/mm/dd) ")
#if he is born 9 mounth,he is unlucky.
print(type(date))
if int(date[:4])>= 2000:

    print("stubborn")
else:

    print("obedient")
#if he born after 2000, he is stubborn,otherwise he is obedient


