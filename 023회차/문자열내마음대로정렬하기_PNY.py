def solution(strings, n):
    answer = [s[n]+s for s in strings]
    answer.sort()
    return [s[1:] for s in answer]
