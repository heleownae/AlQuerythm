#식은 맞으나 시간 초과

def solution(n):
    temp = []
    for x in range(1, n+1):
        if x**2 == n:
            temp.append(x)
    if temp == []:
        return -1
    else:
        return (sum(temp)+1)**2



##나머지 연산자 : 나눌 때 몫을 정수 부분까지만 고려. 소수는 나머지로X
def solution(n):
    root = n**0.5     #정수인지 여부와 관계 없는 제곱근
    if root%1 == 0:    #정수일경우
        return (root+1)**2
    else:                 #정수 아닐 경우
        return -1



