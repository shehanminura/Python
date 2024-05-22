dic={'cham':89,'dil':90,'fgh':87,True:'tyhj',(7,8):True} #LIST wanas kara haka [] namuth tapal wenas kara nohaka
print(dic)
#print([disc[1]])
print(dic['dil'])
#print(dic[90])
dic['cham']=56
print(dic)
dic[87]='sdfgh'
print(dic)
#dic.pop('chamiui')
print(dic.pop('cham'))
print('dic key=',dic.keys(),',list:',list(dic.keys()))
print(dic.values())
print(dic.items())
print(type(dic))
print(type(dic.keys()))
print(type(dic.items()))
print(len(dic))
dic.clear()
print(dic)
#del(dic)
print(dic) # name 'dic' is not defined

print('hiiiii')
my_dict={'a':1,'b':2,'c':3}
#implicitly iterating over items using tuple unpacing
for i in my_dict.items():
    print(f'Key :{i}')

for i in my_dict.values():
    print(f'value:{i}')

for i,j in my_dict.items():
    print(f'key:{1},value:{j}')

for i in my_dict.items():
    print(f'key & value: {i}')
print(my_dict.items())
#print(my_dict.items[0])#TypeError: dict.items() takes no arguments (1 given)
print(list(my_dict.items())[0])
print(list(list(my_dict.items())[0]))
