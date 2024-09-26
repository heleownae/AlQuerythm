def solution(s):
    flag=0
    first=0
    other=0
    result=0
    for i in s:
        if flag==0:
            num = i
            flag+=1
        if i == num:
            first+=1
        else:
            other+=1
        if first==other:
            result+=1
            first=0
            other=0
            flag=0
    if first >=1 or other>=1:
        result+=1
    return result
