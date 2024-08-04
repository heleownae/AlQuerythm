def solution(sizes):
    w = 0
    h = 0
    for i in sizes:
        if w < max(i):
            w = max(i)
        if h < min(i):
            h = min(i)  
    return w * h

# 줄이기
def solution(sizes):
    w = max(max(i) for i in sizes)
    h = max(min(j) for j in sizes)
    return w * h
