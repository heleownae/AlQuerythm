# ???
def solution(s):
    result=[]
    num = 0
    for i in s:
        if num%2==0:
            result.append(i.upper())
        else:
            result.append(i.lower())
        num+=1
    return ''.join(result)

# 재도전!
def solution(s):
    result=[]
    num = 0
    for i in s:
        if i==' ':
            result.append(' ')
            num = 0
        else:
            if num%2==0:
                result.append(i.upper())
            else:
                result.append(i.lower())
            num+=1
    return ''.join(result)
