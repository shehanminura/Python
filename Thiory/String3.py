name="chamanda"

print(name.index("a"))
print(name.index("a",0,3))
print(name)
print(name.index("a",-3))
print(name.index("a",3))
print(name.index("a",3,6))
print(name.index("a",2,-2))
#print(name.index("z"))Traceback (most recent call last):
print('find')
print(name.find("a"))
print(name.find("a",3,6))
print(name.find("z"))
print(name.find("r"))
#name "a" akura nathnam rina agaya enne


print(name.count("a",0,5))    #2
print("a")  #a

#name[2]='d'  # 'str' object does not support item assignment
print(name.replace("a","z",2))   #chzmznda
print(name.replace("a","",1))  #chmanda
print(name.replace("a",''))  #chmnd
print(name.replace("a","zz")) #chzzmzzndzz
print(name.replace("am","bc"))  #chbcanda
print(name.replace("z","a",1))

full_name =' '
print(full_name.isspace())  #True
print(not full_name.isspace())  #False

name="chamanda"


print(name.removeprefix("c"))  #hamanda
print(name.removeprefix('cha')) #manda
print(name.removesuffix("a")) #chamand
print(name.removesuffix("ad")) #chamanda
print(name.removesuffix('da')) #chaman
print(name.removesuffix('m')) #chamanda

print(name[::-1]) #adnamahc
print(name[::-2]) #anmh