'''
def solution(n, lost, reserve):
    reserve = set(reserve) - set(lost)
    lost = set(lost) - set(reserve)
    
    for num in lost:
        if num-1 in reserve:
            reserve.remove(num-1)
        elif num+1 in reserve:
            reserve.remove(num+1)
        else:
            n -= 1
    return n
'''

def solution(n, lost, reserve):
    reserve2 = set(reserve) - set(lost)
    lost2 = sorted(set(lost) - set(reserve))
    
    for num in lost2:
        if num-1 in reserve2:
            reserve2.remove(num-1)
        elif num+1 in reserve2:
            reserve2.remove(num+1)
        else:
            n -= 1
    return n
