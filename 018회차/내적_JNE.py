def solution(a, b):
# 내적 : 요소들을 곱한 후, 모두 더한 값
    return sum(a[i] * b[i] for i in range(len(a)))
