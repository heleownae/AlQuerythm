def solution(arr, divisor):
# arr % divisor == 0 인 elements 담기
	answer = [a for a in arr if a % divisor == 0]
  # answer의 elements 갯수를 확인하여 정렬된 answer 나 -1 출력
  return sorted(answer) if len(answer) > 0 else [-1]

# 더 줄이기    
def solution(arr, divisor):
# 리스트가 비었으면 -1 아니면 리스트 출력
  return sorted([a for a in arr if a % divisor == 0]) or [-1]
