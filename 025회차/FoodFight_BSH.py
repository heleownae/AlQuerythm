def solution(food):
    result=[]
    water=[0]
    for i,j in enumerate(food):
        print(i,j)
        if i >= 1:
            answer = divmod(food[i],2)
            tmp_list = []
            tmp_list.append(i)
            result = result + (tmp_list*answer[0])
    result = result + water + list(reversed(result))
    result = ''.join(map(str, result))
    return result
