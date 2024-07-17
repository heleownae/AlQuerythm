def solution(s):
    l = len(s)
    return True if (l == 4 or l == 6) and s.isdecimal() else False
