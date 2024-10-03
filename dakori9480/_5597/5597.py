student : list = []
late : list = []

for i in range(1,29):
    a = int(input())
    student.append(a)
    
for i in range(1,31):
    if i not in student:
        late.append(i)

print(late[0])
print(max(late))




        