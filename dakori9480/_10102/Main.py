lst : list = []
v = int(input())
result = input()

for i in range(v):
    lst.append(result[i])
    
a = lst.count('A')
b = lst.count('B')
if a>b:
    print("A")
elif a<b:
    print('B')
else:
    print('Tie')