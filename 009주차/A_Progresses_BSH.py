def solution(progresses, speeds):
    import numpy as np
    first=[]
    second=[]
    last=[]
    num=1
    result=[]

    for a in range(len(progresses)):
        first.append(np.ceil((100-progresses[a])/speeds[a]))

    for i in first:
        if len(second)==0:
            second.append(i)
        else:
            if second[-1] >= i:
                second.append(second[-1])
            else:
                second.append(i)

    for e in second:
        if len(last)==0:
            last.append(e)
        else:
            if last[0]==e:
                num+=1
            else:
                result.append(num)
                last.pop()
                last.append(e)
                num=1
    result.append(num)

    return result
