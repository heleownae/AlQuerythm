def solution(s):
    count_trans = 0  
    count_zero = 0  

    while s != "1":
        zeros = s.count('0')
        count_zero += zeros
        s = s.replace('0', '')
        length = len(s)
        s = bin(length)[2:] 
        count_trans += 1 

    return [count_trans, count_zero]
