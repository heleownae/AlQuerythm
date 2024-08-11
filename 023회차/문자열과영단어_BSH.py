def solution(s):
    result = []
    answer = []
    for i in s:
        if i.isdecimal():
            answer.append(i)
        else:
            result.append(i)
            word = ''.join(result)
            if word == 'zero':
                answer.append('0')
                result = []
            elif word == 'one':
                answer.append('1')
                result = []
            elif word == 'two':
                answer.append('2')
                result = []
            elif word == 'three':
                answer.append('3')
                result = []
            elif word == 'four':
                answer.append('4')
                result = []
            elif word == 'five':
                answer.append('5')
                result = []
            elif word == 'six':
                answer.append('6')
                result = []
            elif word == 'seven':
                answer.append('7')
                result = []
            elif word == 'eight':
                answer.append('8')
                result = []
            elif word == 'nine':
                answer.append('9')
                result = []
    return int(''.join(answer))
