def solution(X, Y):

    str_X = str(X)
    str_Y = str(Y)
    
    count_X = [0] * 10
    count_Y = [0] * 10
    
    for xn in str_X:
        count_X[int(xn)] += 1
        
    for yn in str_Y:
        count_Y[int(yn)] += 1
    
    #공통 숫자 찾기
    common = []
    
    for i in range(10):
        if count_X[i] > 0 and count_Y[i] > 0:
            # 공통 숫자의 개수만큼 추가
            common_count = min(count_X[i], count_Y[i])
            common.extend([str(i)] * common_count)
    
    if not common:
        return "-1"  
    elif all(d == '0' for d in common):
        return "0"
    
    # 내림차순
    common.sort(reverse=True)
    
    return ''.join(common)
