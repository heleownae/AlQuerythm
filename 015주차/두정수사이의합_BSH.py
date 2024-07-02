def solution(a, b):
    a1 = sorted([a,b])[0]
    b1 = sorted([a,b])[1]
    return sum(list(range(a1, b1+1)))
