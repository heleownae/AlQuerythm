def solution(n,a,b):
    result = 0
    import math
    while abs(b-a) != 1:
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        result += 1

    return result+1

# 테케 4개 틀림;
