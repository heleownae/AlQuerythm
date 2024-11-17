# 반례 s="  for the what  1what  "

def solution(s):
    result=''
    flag=0

    for i in s:
        if flag==0 and i.isalpha():
            flag=1
            result=result+i.upper()
        else:
            result=result+i.lower()
        if i == ' ':
            flag=0
        else:
            flag=1

    return result
