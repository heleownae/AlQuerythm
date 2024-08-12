def solution(strings, n):
    my_dict = {}
    for i in range(len(strings)):
        my_dict[strings[i]] = strings[i][n]
    sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: (item[1], item[0])))
    return list(sorted_dict_by_value.keys())
