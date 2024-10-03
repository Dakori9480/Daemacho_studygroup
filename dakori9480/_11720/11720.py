count = int(input())
lst : list = []
nums = input()

for i in range(len(nums)):
    lst.append(nums[i])
    
int_num = list(map(int,lst))
print(sum(int_num))
