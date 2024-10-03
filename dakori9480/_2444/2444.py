n = int(input())

# 윗쪽 출력
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i + '*' * (i-1))

# 나머지 출력
for i in range(n - 1, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * i + '*' * (i-1))


    