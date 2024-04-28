name='shehan'
print('My name is '+name)
print('my name is',name)    #( "," magin histhank samaga + vimak sidu wayi)        # my name is shehan
name_2='minura'
print('my name is',name,name_2)         #my name is shehan  minura
print('my signature is',name+name_2)   #my signature is shehanminura
print('my age is',20+7)
# print('my age is'+20+7)   #TypeError: can only concatenate str (not "int") to str

age=27
print('My name is',name,'my age is',age)            #My name is shehan.My age is 27
print(f'My name is {name}.My age is {age}')         #My name is shehan.My age is 27
print('My name is {}  . My age is {}.'. format( name,age))

print(f'My name is {name}.\nMy age is {age}.\nMy second name {name_2}') # "/n" magin print thani paliya . pali 2kakata penwayi
print(name,'\n',age)
print(""" My name is shehan.
                   My age is 27""")
print(f'''My name is {name+name_2}.
                   My age is {age}''')
print(f"My name is {name}",end=' ')   # end=''  magin yata paliya print thani paliyata penwayi
print(name_2)