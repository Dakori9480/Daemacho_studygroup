chess : list = [1,1,2,2,2,8]
piece = list(map(int,input().split()))
result : list = []
for i in range(6):
    if chess[i] - piece[i] == 0:
        result.append('0')
    else:
        result.append(chess[i] - piece[i])
        
for i in range(len(result)):
    print(result[i], end=" ")