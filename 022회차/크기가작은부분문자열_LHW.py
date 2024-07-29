def solution(t, p):
    answer = 0
    lent = len(t)
    lenp = len(p)
    
    for i in range(lent - lenp + 1):
        num = int(t[i:i + lenp])
        
        if num <= int(p):
            answer += 1
        
    return answer
