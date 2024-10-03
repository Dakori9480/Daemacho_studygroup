alpabet: list = list(map(chr, range(97, 123))) # 알파벳 리스트 생성
word = input()
lst : list = [] # 입력한 단어에서 알파벳만 저장
result : list = [-1] * 26 # 알파벳 개수의 -1로 생성된 리스트

for char in word:
    if char in alpabet:
        lst.append(char)  #lst 리스트에 입력한 단어 삽입
        
for i in range(len(lst)):
    index = alpabet.index(lst[i]) # 알파벳의 인덱스를 찾고
    if result[index] == -1: # 해당 인덱스가 -1이라면
        result[index] = i # 인덱스의 값을 result에 저장
    
for i in range(len(result)):
    print(result[i], end=" ")