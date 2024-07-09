def solution(s):
    if len(s) % 2 == 1:
        return list(s)[int(len(list(s))/2)]
    else:
        return list(s)[int(len(list(s))/2)-1] + list(s)[int(len(list(s))/2)]
