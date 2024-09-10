def solution(n, m, section):
    painting = [i for i in range(section[0],section[-1]+1)]
    num=0

    for i in range(len(painting)):
        if section[0] in painting:
            del section[0]
            del painting[:m]
            num+=1
        else:
            del section[0]
        if painting == []:
            break
    # 정확성 38%...
    return num
