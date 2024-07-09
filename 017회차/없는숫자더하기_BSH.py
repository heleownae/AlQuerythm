# 나의 풀이
def solution(numbers):
    answer=[0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        answer.remove(i)
    return sum(answer)

# 지피티의 풀이
def solution(numbers):
    return 45 - sum(numbers)
