def solution(absolutes, signs):
    return sum(absolutes[x] if signs[x] else absolutes[x]*(-1) for x in range(len(absolutes)))
