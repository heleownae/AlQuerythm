def solution(n):
    li=[0,1]

    for i in range(n-1):
        num = li[-2]+li[-1]  # 동적반복
        li.append(num)

    return li[n]%1234567
