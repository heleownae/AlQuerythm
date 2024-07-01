def solution(x):
    number = list(map(int, str(x)))
    if x % sum(number) == 0:
        return True
    else:
        return False
