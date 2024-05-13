while True:
    number = int(input())
    arrayNumber = [] 

    if number == -1:
        break
    
    for i in range(1,number):
        if number % i == 0:
            arrayNumber.append(i)

    result = sum(arrayNumber)        
    if result == number:
        print(result," =",sep='',end='')
        for i in range(len(arrayNumber)-1):
            print(" ",arrayNumber[i]," +",sep='',end='')
        print(" ",arrayNumber[-1],sep='')
    else:
        print(f"{number} is NOT perfect.")