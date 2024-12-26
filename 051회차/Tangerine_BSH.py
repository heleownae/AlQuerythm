from collections import Counter
def solution(k, tangerine):
    result = 0
    a = Counter(tangerine)
    for tan, cnt in a.most_common():  # 요소의 빈도를 기준으로 정렬된 리스트를 반환한다.
        k -= cnt
        result += 1
        if k <= 0 : break
    return result
