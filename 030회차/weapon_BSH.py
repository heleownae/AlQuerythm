def solution(number, limit, power):
    def count_factor(n):
        return sum(2 if n % i == 0 and i != n // i else 1 for i in range(1, int(n**0.5) + 1) if n % i == 0)

    return sum(power if count_factor(i) > limit else count_factor(i) for i in range(1, number + 1))

# 1. 약수의 개수 합을 구하는 함수를 만든다.
# 2. if else문으로 필터링을 한다.
