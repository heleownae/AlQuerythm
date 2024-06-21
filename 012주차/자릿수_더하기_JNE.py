def solution(n):
# 제너레이터 표현식
# 내장함수 안에서 사용할 수 있는 리스트 컴프리헨션 같은 것
  answer = sum(int(i) for i in str(n))
  return answer
