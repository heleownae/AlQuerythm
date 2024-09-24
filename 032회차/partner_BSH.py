'''
# 시간초과: index, remove 문제 -> 시간복잡도 O(n)과 O(n)이 만나 O(n^2)가 됨.
def solution(X, Y):
    result=[]

    for i in X:
        i = int(i)
        Y=list(map(int, Y))
        try:
            Y.index(i)
            Y.remove(i)
            result.append(i)
        except:
            pass

    if result==[]:
        return "-1"
    elif max(result)==0:
        return "0"
    else:
        result.sort(reverse=True)
        return ''.join(map(str,result))
'''

# 개선 방안: 수를 하나하나 확인하지 말고 빈도수로 계산한다.
from collections import Counter

def solution(X, Y):
    result = []
    count_X = Counter(X)
    count_Y = Counter(Y)

    for digit in count_X:
        if digit in count_Y:
            result.extend([digit] * min(count_X[digit], count_Y[digit]))

    if not result:
        return "-1"
    elif max(result) == '0':
        return "0"
    else:
        return ''.join(sorted(result, reverse=True))
