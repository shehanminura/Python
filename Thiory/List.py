marks=[23,67,78,67]
print(marks)
print(type(marks))#list
print(marks[2])#78
print(len(marks))#4
marks[2]=99
print(marks[2])#99
#marks[7]=12
#print(marks) #list assignment index out of range
marks.append(4)
print(marks)#[23, 67, 99, 67, 4]
marks.append('hi')
print(marks)#[23, 67, 99, 67, 4, 'hi']
marks[0]="Hello"
print(marks) #['Hello', 67, 99, 67, 4, 'hi']
student=['shehan',"hasa",'achi','kaushi',]
print(marks+student)#['Hello', 67, 99, 67, 4, 'hi', 'shehan', 'hasa', 'achi', 'kaushi']
print(student.index("achi"))#1
print(student.index('hasa'))#1
print(marks.index(67,0,2))#1
print(marks.index(67,-4,-1))#3
print(marks.count(67))#2
print(marks.pop())#hi mamagin awasana value eka iwath karayi
print(marks)#['Hello', 67, 99, 67, 4]
marks.pop()
print(marks)#['Hello', 67, 99, 67]
marks.pop(1)
print(marks)#['Hello', 99, 67]
marks.remove(67)
print(marks)#['Hello', 99]
marks.extend([56,76])
print(marks)#['Hello', 99, 56, 76]
marks.insert(2,45)
print(marks)#['Hello', 99, 45, 56, 76]
marks2=marks.copy()
print(marks2)#['Hello', 99, 45, 56, 76]
marks.reverse()
print(marks)#[76, 56, 45, 99, 'Hello']
marks2.clear()
print(marks2)#[]
del(marks)
print(marks)#delete list.