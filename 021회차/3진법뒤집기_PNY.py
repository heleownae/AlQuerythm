def solution(n):
    bb = ''
    while n:
        bb += str(n%3) # bb = bb + str(n%3) 과 같은 뜻
        n //= 3
    
    # bb = bb[::-1]   # 위의 4번째 줄 코드가 bb = str(n%3) + bb 일 때만 작동
    
    return int(bb, 3)
