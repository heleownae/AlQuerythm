# 연속 부분 수열 합의 개수
def solution(elements):
    cir = elements * 2
    sums = set()
    
    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            sub_sum = sum(cir[start:start + length])
            sums.add(sub_sum)

    return len(sums)
