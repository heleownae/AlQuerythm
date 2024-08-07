def solution(s):
    num = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 
            'four': '4', 'five': '5', 'six': '6', 'seven': '7', 
            'eight': '8', 'nine': '9'}
    for key, val in num.items():
        s = s.replace(key, val)
    return int(s)

'''
def solution(s):
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for num in range(10):
        s = s.replace(word[num], str(num))
    return int(s)
'''
