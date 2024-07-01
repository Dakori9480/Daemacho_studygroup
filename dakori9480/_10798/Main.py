strings : list = []
result : list = [] # 문자 저장용

for i in range(5):
    addstring = list((input()))
    strings.append(addstring)

# 최대 15글자까지 세로로 읽기
for i in range(15):
    for word in strings: 
        if i < len(word):
            result.append(word[i])

print(''.join(result))
# result는 리스트 이므로 join으로 문자를 이어붙임