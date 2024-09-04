def solution(nums):
    result = []

    # 조합을 만들어서 소수인 경우를 필터링한다.
    import itertools
    answer = [sum(i) for i in list(itertools.combinations(nums, 3))]

    for i in answer:
        yaksu = [e for e in range(2,i) if i%e == 0]
        if yaksu == []:
            result.append(i)

    return len(result)
