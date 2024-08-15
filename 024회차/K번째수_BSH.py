def solution(array, commands):
    result=[]
    for i in commands:
        a=sorted(array[i[0]-1:i[1]])
        result.append(a[i[2]-1])
    return result
