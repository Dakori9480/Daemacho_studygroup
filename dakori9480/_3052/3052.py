remainder : list = [] # 나머지 

for i in range(10):
    a = int(input())
    c = a%42
    remainder.append(c)

index = len(list(set(remainder))) #set은 중복값 삭제
print(index)