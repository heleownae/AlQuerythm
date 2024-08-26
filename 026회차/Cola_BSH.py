def solution(a, b, n):
    result=0
    while n>=a:
        coke=divmod(n,a)[0]*b
        result+=coke
        rest=divmod(n,a)[1]
        total=coke+rest
        n=total
    return result
