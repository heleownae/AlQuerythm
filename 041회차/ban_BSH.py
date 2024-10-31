def solution(id_list, report, k):
    report=list(set(report))  # 미리 정의해서 오답확률을 없앰.
    breaker=[a.split(' ')[1] for a in report]
    from collections import Counter
    breakers=Counter(breaker)
    outer=[key for key,value in breakers.items() if value>=k]

    mailing=[0]*len(id_list)

    for b in report:
        if b.split(' ')[1] in outer:
            mailing[id_list.index(b.split(' ')[0])]+=1

    return mailing
