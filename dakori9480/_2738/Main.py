width, length = map(int,input().split())
matrix : list = []
addnum : list = []
result : list = []

for i in range(width):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(width):
    row = list(map(int, input().split()))
    addnum.append(row)  

for i in range(width):
    result_row = []
    for j in range(length):
        result_row.append(matrix[i][j] + addnum[i][j])
    result.append(result_row)
    
for row in result:
    print(" ".join(map(str, row)))