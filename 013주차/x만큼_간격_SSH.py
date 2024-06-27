def solution(x, n):
    return [i*x for i in range(1, n+1)]


#8번 테스트에서 안 됨..ㅎ
def solution(x, n):
    return [x for x in range(x, n+x, x)]
