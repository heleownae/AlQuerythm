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
