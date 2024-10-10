# 수정 필요
ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
hamburger = [1,2,3,1]
perfect = 0

for i,e in enumerate(ingredient):
    if e == 1:
        if ingredient[i:i+4] is hamburger:
            perpect+=1
