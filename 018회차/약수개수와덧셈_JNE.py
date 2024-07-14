def solution(left, right):
# 제곱근(root)의 제곱이 정수가 되는지 않되는지를 이용해 판별
    return sum(-i if int(i ** 0.5) ** 2 == i else i for i in range(left, right + 1))
