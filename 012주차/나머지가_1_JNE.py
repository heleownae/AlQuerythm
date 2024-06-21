def solution(n):
	answer = 0
	result = []
	# n 이하의 자연수 불러오기
	for i in range(1, n):
	# n을 i로 나눠 1이 되는 것 찾기
		if n % i == 1:
			 result.append(i)
 # 리스트에서 가장 작은 수 뽑아서 출력
	 answer = min(result)
	 return answer
	 
def solution(n):
	answer = min(i for i in range(1, n) if n % i == 1)
	return answer
