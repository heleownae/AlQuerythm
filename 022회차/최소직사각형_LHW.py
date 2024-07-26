def solution(sizes):
    left = []
    right = []
    
    for i in sizes:
        if i[0] >= i[1]:
            left.append(i[0])
            right.append(i[1])
        else:
            right.append(i[0])
            left.append(i[1])
    
    return max(left) * max(right)
