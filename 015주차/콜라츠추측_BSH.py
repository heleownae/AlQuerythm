def solution(n):
    number=0
    while True:
        if n == 1:
            return number
        if n % 2 ==0:
            n = n / 2
            number+=1
        else:
            n = n * 3 + 1
            number+=1
        if number == 501:
            return -1
