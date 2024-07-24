def solution(n):
  num = []
  while n > 0:
  # n을 3으로 나눈 나머지를 저장
      num.append(n % 3)
      # n을 3으로 나눈 몫 저장해서 반복 시키기
      n //= 3
      # 3진법 결과 뒤집기
  num.reverse()
  result = 0
  # enumerate 함수를 이용해 a에 인덱스. b에는 요소 받음
  for a, b in enumerate(num):
	    result += b * (3 ** a)
  return result
   
# 줄이기 
def solution(n):
  num = []
  while n > 0:
      num.append(n % 3)
      n //= 3
  return sum(b * (3 ** a) for a, b in enumerate(num[::-1]))
