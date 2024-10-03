basket : list = []
n, m = map(int,input().split())

for i in range(0,n+1):
    basket.append(i)
    
for a in range(m):
    i,j = map(int,input().split())
    basket[i],basket[j] = basket[j],basket[i]

for b in range(1,len(basket)):
    print(basket[b], end=" ") 