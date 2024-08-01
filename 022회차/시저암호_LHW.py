def solution(s, n):
    result = []
    
    for i in s:
        if i.isupper():
            result.append(chr((ord(i) - ord('A') + n) % 26 + ord('A')))
        elif i.islower():
            result.append(chr((ord(i) - ord('a') + n) % 26 + ord('a')))
        else:
            result.append(i)
    
    return ''.join(result)
