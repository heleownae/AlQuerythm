import math

def solution(arr):
    # 1은 모든 자연수의 약수니까 일단 넣어놈
    # 첫번째 요소의 최소공배수 구하기 위해
    a = 1
    for i in range(len(arr)):
        b = arr[i]
        # arr에서 요소를 하나씩 받아와서 a와 b의 곱을 최대공약수로 나누는 과정 반복 
        a = abs(a * b) // math.gcd(a, b)
    return a
