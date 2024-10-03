# a은 바구니의 개수 / b은 공을 넣는 회수
a,b = map(int,input().split())

# a+1 길이의 요소가 모두 0인 리스트 생성
baskets : list = [0] * (a+1)  

# i 바구니 부터 j바구니 까지 k번 공을 넣는다
for second in range(b):
    i,j,k = map(int,input().split())
    for third in range(i,j+1): 
        baskets[third] = k

# 0번 리스트부터 baskets의 요소개수만큼 반복해서 출력
for fourth in range(1,len(baskets)): # 0번째 리스트는 출력 X
    print(baskets[fourth], end=' ') 