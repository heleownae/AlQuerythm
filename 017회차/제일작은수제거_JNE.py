def solution(arr):
# 리스트 길이가 1개 이하이면 [-1] 출력
# 아니면 조건 수행
    return [-1] if len(arr) <= 1 else (arr.remove(min(arr)) or arr)
