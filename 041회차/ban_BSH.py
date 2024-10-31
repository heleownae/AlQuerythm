# 테스트 케이스 외 실패
def solution(id_list, report, k):
    breaker=[a.split(' ')[1] for a in list(set(report))]
    from collections import Counter
    breakers=Counter(breaker)
    outer=[key for key,value in breakers.items() if value>=k]

    mailing=[0]*len(id_list)

    for b in report:
        if b.split(' ')[1] in outer:
            mailing[id_list.index(b.split(' ')[0])]+=1

    return mailing
