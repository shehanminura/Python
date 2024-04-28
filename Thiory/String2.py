     #654321
name="shehan"
    # 012345
print("a" in name) #True
if ("a" in name):
    print("yor are lucky")
print("he" in name) #true
print("ha" in name) #True
print("sn" in name) #false


print(name[0])
print(name[1])
print(name[5])
#print(name[10]) IndexError: string index out of range
print(name[-1])
print(name[-2])
print(name[-3])
print(name[0].isdigit())   #false
print(name[0].isalpha())   #true
#print[0]="s"   #error
#print(name)

print(name[0].isupper())    #flase
#name[0]=name[0].upper()   'str' object does not support item assignment
#print(name[0])

print(name[0:2])  #sh
print(name[1:4])  #heh
print(name[3:])     #han
print(name[:4])   #sheh
print(name[-4:-1])      #eha
print(name[-4:])     #ehan
print(name[:-2])     #sheh
print(name[2:-2])         #eh
print("###",name[-2:-4])
print("@@@",name[3:0])