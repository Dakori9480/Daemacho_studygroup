result : list = []   # 리스트 = 책꽂이
for i in range(9):   # 9번 반복
    a = int(input())      # 사용자의 입력을 받음 
    result.append(a) # 리스트안에 a의 값을 집어넣음
                     # 책꽂이에 책 꽂기
count = max(result)  # 책중 가장 비싼책 고르기 
print(count)         # 가장 비싼책의 가격을 출력
print(result.index(count) + 1 )  # 그 비싼책의 순번을 출력 