def solution(s):
    answer = ''
    a = 0
    
    for i in s:
        if i == ' ':
            answer += ' '
            a = 0
        else:
            if a % 2 == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            a += 1
            
    return answer
