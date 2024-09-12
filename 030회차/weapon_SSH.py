#시간초과

def solution(number, limit, power):
    # 약수의 개수를 구하는 함수
    def get_divider_n(a):
        count = 0
        for i in range(1, a + 1):
            if a % i == 0:
                count += 1
        return count

    # 각 숫자에 대해 약수의 개수를 구하고, 제한된 수를 초과하면 power로 대체
    temp = [min(get_divider_n(x), power) if get_divider_n(x) > limit else get_divider_n(x) for x in range(1, number + 1)]
    
    return sum(temp)



###약수 구할 때 제곱근만 바꾸면 됨
