def solution(n):
    y = n-1
    
    for i in range(n-2, 1, -1):
        if n % i == 1 and n % i < y:
            y = i
    return y
