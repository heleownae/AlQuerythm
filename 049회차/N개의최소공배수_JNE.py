import math

def solution(arr):
    a = 1
    for i in range(len(arr)):
        b = arr[i]
        a = abs(a * b) // math.gcd(a, b)
    return a
