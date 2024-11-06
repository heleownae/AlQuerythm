def solution(s):
    num = sorted(map(int, s.split()))
    return f"{min(num)} {max(num)}"
