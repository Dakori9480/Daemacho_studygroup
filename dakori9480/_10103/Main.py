round = int(input()) 
firstScore, secondScore = 100, 100

for i in range(round):
    firstNum, secondNum = map(int,input().split())
    
    if firstNum > secondNum:
        secondScore -= firstNum
        
    elif firstNum < secondNum:
        firstScore -= secondNum
        
    else:
        continue
    
print(firstScore)
print(secondScore)