# 실패
# 같은 라운드의 다른 매치일때도 진행이 됨
import math

def solution(n, a, b):
    answer = 0
    while abs(a - b) != 1:
        a = math.ceil(a / 2) 
        b = math.ceil(b / 2)  
        answer += 1
    return answer

# 성공
def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2 
        answer += 1
    return answer
