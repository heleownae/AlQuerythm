def solution(sizes):
    h = []
    w = []
    for i in sizes:
        h.append(max(i))
        w.append(min(i))
    return max(h)*max(w)
