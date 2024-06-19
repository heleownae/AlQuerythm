def solution(num):
	# 홀수, 짝수는 2로 나누었을 때, 나머지가 각 각 1, 0의 여부로 나눌 수 잇음
  if num % 2 == 0:
      answer = 'Even'
  else:
      answer = 'Odd'
  return answer
  # 마지막 조건 역시 0을 어떤 수로 나누든지 항상 몫과 나머지는 0일 것이기 때문에 자동으로 충족
