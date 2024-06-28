# 제곱근 모듈이 필요해서 math import
import math
def solution(n):
    answer =  int(math.sqrt(n))
    if n == answer ** 2:
        return (answer + 1) ** 2
    else:
        return -1
