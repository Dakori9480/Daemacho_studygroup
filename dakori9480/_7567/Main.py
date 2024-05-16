setting : int = 10
bowl = input()
bowl_list : list = []

for i in range(len(bowl)):
    bowl_list.append(bowl[i])

for i in range(len(bowl_list)-1):
    if bowl_list[i] == bowl_list[i+1]:
        setting += 5
    else:
        setting += 10
        
print(setting)