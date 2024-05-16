case = int(input()) # 테스트 케이스의 개수

for i in range(case):
    school = int(input()) # 학교의 개수
    
    for j in range(school):
        schoolData = {} # 빈 딕셔너리
        
    for k in range(school):
        name, drink = input().split()  # 데이터를 입력받고
        schoolData[name] = int(drink)  # 딕셔너리에 키와 밸류값을 대입
    maxSchool = max(schoolData, key=schoolData.get)  # 딕셔너리중 가장 큰 값의 키를 저장
    print(maxSchool)
    
