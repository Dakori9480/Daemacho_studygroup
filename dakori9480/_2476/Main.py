array : list = []

count = int(input())

for i in range(count):
    a,b,c = map(int,input().split())
    if(a==b==c):
        array.append(10000 + a * 1000)
    elif(a==b or a==c):
        array.append(1000 + a * 100)
    elif(b==c):
        array.append(1000 + b * 100)
    else:
        array.append(max(a,b,c)*100)

array.sort()
print(array[-1])