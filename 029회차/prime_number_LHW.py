# 소수 T/F 확인하는 함수
def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    count = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                sum_comb = nums[i] + nums[j] + nums[k]
                if isprime(sum_comb):
                    count += 1
    return count
