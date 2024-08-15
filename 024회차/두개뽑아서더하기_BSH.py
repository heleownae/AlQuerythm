def solution(numbers):
    import itertools
    return sorted({i[0]+i[1] for i in list(itertools.combinations(numbers,2))})
