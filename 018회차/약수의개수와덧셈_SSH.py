def solution(left, right):
    result = 0
    for x in range(left, right+1, 1):
      if len([n for n in range(1, x+1, 1) if x%n==0])%2 == 0:
        result += x
      else:
        result -= x
    return result
        
