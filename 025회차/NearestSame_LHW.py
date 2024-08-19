def solution(s):
    a = {}
    answer = []

    for i, j in enumerate(s):
        try:
            index = a[j]
            answer.append(i - index)
            a[j] = i
        except:
            a[j] = i
            answer.append(-1)
    
    return answer
