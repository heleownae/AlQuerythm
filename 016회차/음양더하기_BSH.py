def solution(absolutes, signs):
    return sum([a if b==True else -a for a, b in zip(absolutes, signs)])
