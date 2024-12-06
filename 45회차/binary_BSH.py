def solution(s):
    remove_zero = 0
    ch_2 = 0

    while True:
        tmp_1 = len(s)
        tmp_2 = list(filter(lambda x: x not in '0',s))
        tmp_3 = len(tmp_2)
        remove_zero = remove_zero + tmp_1-tmp_3
        s = bin(tmp_3)[2:]
        ch_2 += 1

        if s == '1':
            break

    return [ch_2,remove_zero]
