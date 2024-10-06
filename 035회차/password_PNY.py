def solution(s, skip, index):
    answer = ''
    import string
    alpha = set(string.ascii_lowercase)
    skip = set(skip)
    letters = sorted(alpha-skip)
    
    for a in s:
        n = letters.index(a)
        m = (n+index) % len(letters)
        answer += letters[m]
        
    return answer
