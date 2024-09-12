def solution(n, m, section):
    answer = 0
    a = 0   # 마지막 위치 저장
    
    for s in section:
        if a < s:
            answer += 1
            a = s + m - 1   # 마지막 위치 갱신
            
    return answer
