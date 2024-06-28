def solution(n):
    result = list(str(n))
# 내림차순 정렬
    result.sort(reverse= True)
# 문자열을 결합 후 정수로 반환
    return int(''.join(result))
