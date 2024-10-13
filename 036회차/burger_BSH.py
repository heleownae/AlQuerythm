# 수정 필요
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
hamburger = [1,2,3,1]
perfect = 0

for i,e in enumerate(ingredient):
    if e == 1:
        if ingredient[i:i+4] is hamburger:
            perpect+=1

# 수정 완료
def solution(ingredient):
    hamburger = [1,2,3,1]
    temp = []
    makeit = 0
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == hamburger:
            makeit += 1
            del temp[-4:]
    return makeit
