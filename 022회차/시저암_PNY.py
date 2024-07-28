def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        else:
            a = ord(i) + n
            if (i.isupper() and a > ord('Z')) or (i.islower() and a > ord('z')):
                a -= 26
            answer += chr(a)
        
    return answer
