def solution(cards1, cards2, goal):
    c1=[]
    c2=[]

    for i in goal:
        try:
            c1.append(cards1.index(i))
        except:
            c2.append(cards2.index(i))

    if (sorted(c1) == c1) & (sorted(c2) == c2):
        return "Yes"
    else:
        return "No"  # 예외경우 1케이스
