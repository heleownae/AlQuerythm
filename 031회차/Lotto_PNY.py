'''
def solution(lottos, win_nums):
    answer = []
    win = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    same = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    
    if zero == 0:
        answer.extend([win.get(same), win.get(same)])
    elif zero == 1:
        answer.extend([win.get(same+1), win.get(same)])
    elif zero == 2:
        answer.extend([win.get(same+2), win.get(same)])
    elif zero == 3:
        answer.extend([win.get(same+3), win.get(same)])
    elif zero == 4:
        answer.extend([win.get(same+4), win.get(same)])
    elif zero == 5:
        answer.extend([win.get(same+5), win.get(same)])
    else:
        answer.extend([1,6])
    
    return answer
'''

def solution(lottos, win_nums):
    win = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    same = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)
    
    max_rank = win.get(same+zero)
    min_rank = win.get(same)
    
    return [max_rank, min_rank]
