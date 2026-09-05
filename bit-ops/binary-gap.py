def binary_gap(N):
    result = bin(N)[2:]
    flag = False
    count = 0
    gap = 0
    
    for number in result:
        if number == "1" and not flag:
            flag = True
        elif number == "1" and flag:  
            if count > gap:
                gap = count
            count = 0
        elif number == "0" and flag:
            count += 1
    return gap