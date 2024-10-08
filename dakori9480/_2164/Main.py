# 내가 작성한 코드

# pop의 시간 복잡도는 O(n)이기에 n이 커질수록 시간이 오래걸림

"""
inputNumber = int(input())
array = []
for i in range(1, inputNumber+1):
    array.append(i)
    
while (len(array) > 1):
    array.pop(0)
    array.append(array.pop(0))
    
print(array[0])
"""
# 해결방법은 deque 를 사용해 시간복잡도를 줄이는 방법!

from collections import deque

inputNumber = int(input())
array = deque(range(1, inputNumber+1))

while len(array) > 1:
    array.popleft() 
    array.append(array.popleft())  # 두 번째 요소를 맨 뒤로 이동

print(array[0]) 

