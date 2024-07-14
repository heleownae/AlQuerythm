def solution(left, right):
    result=[]
    for i in range(left,right+1):
        num=[e for e in range(1,i+1) if i%e==0]
        if len(num)%2==0:
            result.append(i)
        else:
            result.append(-i)

    return sum(result)
