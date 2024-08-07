def solution(price, money, count):
    need = price * (count * (count+1) / 2) - money
    return max(0, need)

'''
필요 금액(need) = 총이용료 - 현재 금액(money)
총이용료 = 이용료(price) * (1+2+...+횟수(count))

--- case 1 ---------------------------------------
count = 4,

   1+2+3+4
+  4+3+2+1
----------
   5+5+5+5  = 5*4 = n(n+1)

1+2+3+4 = n(n+1)/2 = (4*5)/2 = 10
--------------------------------------------------

--- case 2 ---------------------------------------
count = 1,

   1
+  1
----------
   2  = 1*2 = n(n+1)

1 = n(n+1)/2 = (1*2)/2 = 1
--------------------------------------------------

총이용료 = 이용료(price) * (count * (count+1) / 2)
'''
