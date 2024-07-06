def solution(arr, divisor):
    answer = sorted([x for x in arr if x%divisor == 0])
    if len(answer) == 0:
        return [-1]
    else:
        return answer
