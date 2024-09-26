def solution(n, lost, reserve):
    
    lost_o = set(lost) - set(reserve)
    reserve_o = set(reserve) - set(lost)
    
    for i in reserve_o:
        if i - 1 in lost_o:
            lost_o.remove(i - 1)
        elif i + 1 in lost_o:
            lost_o.remove(i + 1)
        
    answer = n - len(lost_o)
    
    return answer
