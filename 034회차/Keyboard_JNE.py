def solution(keymap, targets):
    char_to_presses = {}
    
    for key_number, key in enumerate(keymap):
        for press_number, char in enumerate(key):
            if char not in char_to_presses:
                char_to_presses[char] = press_number + 1  # +1은 0-indexed 때문
            else:
                char_to_presses[char] = min(char_to_presses[char], press_number + 1)
    
    result = []
    
    for target in targets:
        total_presses = 0
        for char in target:
            if char in char_to_presses:
                total_presses += char_to_presses[char]
            else:
                total_presses = -1
                break
        result.append(total_presses)
    
    return result
