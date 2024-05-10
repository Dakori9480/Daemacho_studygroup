countA = 0
countB = 0
countC = 0

time = int(input())

while True:
    if time < 300:
        break
    else:
        time -= 300
        countA += 1

while True:
    if time < 60:
        break
    else:
        time -= 60
        countB += 1

while True:
    if time < 10:
        break
    else:
        time -= 10
        countC += 1

if time != 0:
    print("-1")
else:
    print("{} {} {}".format(countA,countB,countC))