standard = -1
row = 0
col = 0
array = [list(map(int, input().split())) for _ in range(9)] # 2차원 배열 9x9 생성

for i in range(9):
    for j in range(9):
        if array[i][j] > standard:
            standard = array[i][j]
            row = i + 1
            col = j + 1

print(standard)
print(row, col)