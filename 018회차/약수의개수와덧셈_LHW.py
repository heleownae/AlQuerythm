def solution(left, right):
    return sum(-n if int(n**0.5) ** 2 == n else n for n in range(left, right + 1))
