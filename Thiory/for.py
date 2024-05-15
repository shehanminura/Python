i=0
while (i<7):
    print(i)
    i+=1

for i in range (7):
    print(i)

for i in range (2,7):
    print(i)

for i in range (2,10,2):
    print(i)

for i in range (2,10,3):
    print(i)

for i in range (10,2,-3):
    print(i)

for i in range (8,2,-3):
    print(i)

student_marks =[30,45,75,56]
for mark in student_marks:
    print(mark)  

student_marks =[30,45,75,56]
new_student_marks=[]
for mark in student_marks:
    new_student_marks.append(mark+5)
print(new_student_marks)