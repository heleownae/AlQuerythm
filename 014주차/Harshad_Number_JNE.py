def solution(x):
# x의 각 자리 수 합을 구함
    a = sum(int(b) for b in str(x))
    # 하샤드 수 판별
    if x % a == 0:
        return True
    else:
        return False
