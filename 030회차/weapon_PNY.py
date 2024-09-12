def c_divisor(n):  # 약수의 개수 구하는 함수
    count = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


def solution(number, limit, power):
    div_list = []
    
    for n in range(1, number+1):
        div = c_divisor(n)
        if div > limit:
            div_list.append(power)
        else:
            div_list.append(div)
        
    return sum(div_list)
