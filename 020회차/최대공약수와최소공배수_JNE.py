def solution(n, m):
    answer = []
    for a in range(1, min(n, m) + 1):  
        if n % a == 0 and m % a == 0:
            answer.append(a)
    gcd = max(answer)     
    lcm = (n * m) // gcd 
    return gcd, lcm  
    
def solution(n, m):
    gcd = max(a for a in range(1, min(n, m) + 1) if n % a == 0 and m % a == 0)
    lcm =  (n * m) // gcd
    return [gcd, lcm]
