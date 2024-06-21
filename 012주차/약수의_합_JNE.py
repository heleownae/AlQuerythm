def solution(n):
	 answer = 0 
	 # n 이하의 모든 자연수 불러옴
	 for i in range(1, n+1):
	 # n을 각 각의 수로 하나씩 나눠 줌
		 if n % i == 0
			 answer += i
	 return answer
	 
def solution(n):
  answer = sum(i for i in range(1, n+1) if n % i == 0)
  return answer
