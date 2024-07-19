def solution(n, m):
    a = 0  #최대공약수
    
    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
            a = i

    b = int(n * m / a)  #최소공배수
    answer = [a, b]
    
    return answer
