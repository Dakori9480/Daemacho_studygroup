case = int(input())

for i in range(case):
    note = input()
    score = 0
    count = 0
    
    for result in note:
        if result == 'O':
            count += 1
            score += count
        else:
            count = 0
    
    print(score)