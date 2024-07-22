# 테스트에선 작동하는데 결과는 오류남. 문법 문제라고 함.
def solution(arr1, arr2):
  li = list(zip(arr1, arr2))
  result=[]
  for i, e in li[0], li[1]:
    result.append([i[o]+e[o] for o in range(len(i))])
  return result

# zip쓰면 맞음.
def solution(arr1, arr2):
  return [[x + y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)]
