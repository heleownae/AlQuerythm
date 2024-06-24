def solution(n):
# str()로 숫자를 하나씩 분리한 다음 역방향으로 int()에 삽입
    return [int(a) for a in str(n)[::-1]]
