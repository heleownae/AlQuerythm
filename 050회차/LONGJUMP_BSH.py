def solution(n):
    before = 1
    defult = 1
    after = 1
    for i in range(n-1):
        if i == 0:
            before += defult
        else:
            before += after
            after += 1
    return before % 1234567  # ?
