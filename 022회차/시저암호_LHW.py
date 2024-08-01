def solution(s, n):
    answer = []
    
    for i in s:
        if i.isupper():
            answer.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
        elif i.islower():
            answer.append(chr((ord(i) - ord('a') + n) % 26 + ord('a')))
        else:
            answer.append(i)
    
    return ''.join(answer)
