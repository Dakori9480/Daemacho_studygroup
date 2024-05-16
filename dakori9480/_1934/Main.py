test = int(input())

for i in range(test):
    x,y = map(int,input().split())
    
# 최대공약수
    a, b = x, y
    while b:
        a, b = b, a % b 

# 최소공배수는 X와Y를 곱한 후 최대 공약수로 나눔
    result = (x * y) // a
    print(result)