while True:
    fir_num, sec_num = map(int,input().split())
    if fir_num == sec_num == 0:
        break
    if fir_num < sec_num:
        if sec_num % fir_num == 0:
            print("factor")
        else:
            print("neither")
    elif fir_num > sec_num:
        if fir_num % sec_num == 0:
            print("multiple")
        else:
            print("neither")