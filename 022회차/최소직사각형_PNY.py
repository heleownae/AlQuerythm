def solution(sizes):
    a, b = 0, 0
    
    for i in sizes:
        long, short = max(i), min(i)
        a = max(a, long)
        b = max(b, short)
            
    return a*b
