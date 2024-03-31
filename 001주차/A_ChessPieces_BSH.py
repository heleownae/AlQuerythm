problem = [2, 1, 2, 1, 2, 1]

def chess_finder(chesS_list):
    result = []
    for num, i in enumerate(chesS_list):
        if num in [0,1]:
            result.append(1-i)
        elif num in [2,3,4]:
            result.append(2-i)
        else:
            result.append(8-i)
    return result
