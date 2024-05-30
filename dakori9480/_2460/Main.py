inList : list = []  # 탄 사람
outList : list = [] # 내린 사람
maxMember : list = [] # 두 리스트의 차를 저장할 리스트

for i in range(10):
    outTrain, inTrain = map(int,input().split())
    
    sum_in = sum(inList)
    sum_out = sum(outList)
    
    inList.append(inTrain)
    outList.append(outTrain)
    maxMember.append(sum_in - sum_out)
    
print(max(maxMember))