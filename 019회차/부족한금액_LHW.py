def solution(price, money, count):
    a = sum(price * i for i in range(1, count+1))
    b = a - money
    return b if b > 0 else 0
