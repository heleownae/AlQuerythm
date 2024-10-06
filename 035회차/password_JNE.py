def solution(s, skip, index):
    result = []
    skip_set = set(skip)
    current_index = 0  

    for char in s:
        while current_index < index:
            char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            if char not in skip_set:
                current_index += 1 
        
        result.append(char)
        current_index = 0 

    return ''.join(result)
