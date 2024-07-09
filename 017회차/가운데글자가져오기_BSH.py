def solution(s):
    n = int(len(list(s))/2)
    return s[n] if len(s) % 2 == 1 else s[n-1:n+1]
