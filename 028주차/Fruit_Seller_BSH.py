# 일부 시간초과ㅠ
def solution(k, m, score):
    answer=[]
    result=[]

    score.sort(reverse=True)

    while True:
        for i in range(m):
            tmp = score.pop(0)
            answer.append(tmp)

        result.append(min(answer)*m)
        answer=[]

        if len(score)<m:
            break

    return sum(result)
