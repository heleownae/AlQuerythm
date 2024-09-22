'''
# 시간 초과
def solution(X, Y):
    answer = []
    X = list(X)
    Y = list(Y)

    for x in X:
        if x in Y:
            Y.remove(x)
            answer.append(x)
    
    if not answer:
        return '-1'
    elif set(answer) == {'0'}:
        return '0'
    else:
        answer.sort(reverse=True)
        return ''.join(answer)
'''

def solution(X, Y):
    answer = ''

    for i in range(9, -1, -1):
        answer += str(i) * min(X.count(str(i)), Y.count(str(i)))
    
    if not answer:
        return '-1'
    elif set(answer) == {'0'}:
        return '0'
    else:
        return answer
