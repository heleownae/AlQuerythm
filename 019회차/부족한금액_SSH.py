def solution(price, money, count):
    answer = sum([price*i for i in range(count +1)]) - money
    return answer if answer > 0 else 0 
