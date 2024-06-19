def solution(arr):
# 평균은 요소의 합을 요소의 갯수로 나누어주면 됨
# sum 함수를 이용해 합을 구한 후 len함수를 이용해 갯수를 구해 나눔 
	answer = sum(arr) / len(arr)
  return answer
