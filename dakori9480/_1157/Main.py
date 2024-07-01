word = input().upper()
count : dict = {}

for value in word: 
    try: count[value] += 1
    except: count[value] = 1

maxNum = max(count.values())
maxChar = [value for value, freq in count.items() if freq == maxNum]
# count.items를 사용해 키-값을 value,freq에 저장
# freq랑 maxNum이 같으면 그 값에 해당하는 키를 리스트에 추가
if len(maxChar) > 1:
    print("?")
else:
    print(maxChar[0])