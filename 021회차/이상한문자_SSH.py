def solution(s):
    answer = []
    worlds = s.split(' ')
    for a in worlds:
        tmp = ''
        for i, l in enumerate(a):
            if i == 0 or i%2 == 0:
                tmp += l.upper()
            else:
                tmp += l.lower()
        answer.append(tmp)
    return " ".join(answer)
