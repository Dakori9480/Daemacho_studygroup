basket = []

n, m = map(int, input().split())
for i in range(n):
    basket.append(i + 1)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1  # 2를 고치려면 1번 인덱스에 접근해야 함
    b -= 1
    while a < b:  # a가 b보다 작을 때까지 반복
        basket[a], basket[b] = basket[b], basket[a]
        a += 1
        b -= 1

for i in range(len(basket)):
    print(basket[i], end=" ")
