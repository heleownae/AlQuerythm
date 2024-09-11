#시간초과

def solution(n, m, section):
    temp = section[:]
    count = 0
    while temp:
        temp2 = [b for b in range(min(section), m+1)]
        temp = [x for x in temp if x not in temp2]
        count += 1
    else:
        return count




def solution(n, m, section):
    count = 0
    i = 0
    while i < len(section):
        count += 1
        # 현재 위치 section[i]를 시작으로 m 범위를 덮음
        start = section[i]
        # start + m까지 덮을 수 있으므로 그 범위 안에 있는 항목들을 무시하고 넘어감
        while i < len(section) and section[i] < start + m:
            i += 1
    return count

