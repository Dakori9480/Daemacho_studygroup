pointArray : list = [] # 좌표를 모을 리스트

for i in range(3):
    pointArray.append(list(map(int, input().split())))

# 첫 번째와 두 번째의 벡터 계산
x1 = pointArray[1][0] - pointArray[0][0]
y1 = pointArray[1][1] - pointArray[0][1]

# 두 번째와 세 번째의 벡터 계산
x2 = pointArray[2][0] - pointArray[1][0]
y2 = pointArray[2][1] - pointArray[1][1]

if y1 > 0:
    if x2 < 0:
            print(1)
    else:
            print(-1)
else:
    if x2 < 0:
            print(-1)
    else:
            print(1)
       
if y1 * x2 > 0 :
    print(-1)
if y1 * x2 < 0 :
    print(1)
