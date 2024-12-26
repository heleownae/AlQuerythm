from collections import Counter
def solution(k, tangerine):
    result = 0
    a = Counter(tangerine)
    for tan, cnt in a.most_common():
        k -= cnt
        result += 1
        if k <= 0 : break
    return result
