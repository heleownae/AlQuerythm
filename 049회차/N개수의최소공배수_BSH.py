def solution(arr):
    answer=0
    arr=sorted(arr)
    for i in range(len(arr)-1):
        arr1 = arr.pop(-1)
        arr2 = arr.pop(-1)
        result = [arr1, arr2]
        result = sorted(result)
        arr1 = result[-1]
        arr2 = result[-2]
        tmp = arr1*arr2
        print(arr1, arr2)
        while True:
            arr3 = arr1%arr2
            if arr3 == 0:
                answer = tmp//arr2
                arr.append(answer)
                break
            else:
                arr1=arr2
                arr2=arr3

    return answer

# 더 쉬운 방법이 있다.

def solution(arr):
    import math

    # 1. 두 수씩 최소공배수를 계산한다.
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)  # 최대공약수 gcd

    # 2. 배열의 최소공배수를 계산한다.
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer
