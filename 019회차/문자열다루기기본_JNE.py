def solution(s):
# isdigit() : 문자열이 숫자로만 구성되어 있는지를 직접 확인
# and 연산자를 이용해 2조건 모두 충족 여부 판단
    return len(s) in (4, 6) and s.isdigit()
