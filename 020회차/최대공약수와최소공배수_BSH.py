def solution(n, m):
    c = [i for i in range(1, n+1) if n%i == 0]
    d = [i for i in range(1, m+1) if m%i == 0]
    e = max(list(set(c)&set(d)))
    f = int((n*m)/e)
    return [e,f]
