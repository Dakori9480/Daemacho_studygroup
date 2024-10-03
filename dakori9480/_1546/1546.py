def divBymax(x): return x / max(lst) * 100

subject = int(input())
lst: list = [0] * subject
lst = list(map(int, input().split()))

average = list(map(divBymax, lst))
total = sum(average) / len(average)

print(total)