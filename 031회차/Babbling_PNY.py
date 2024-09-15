'''
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for s in babbling:
        double_check = True
        for word in words:
            if word * 2 in s:
                double_check = False
                break
                
        if double_check:
            s = s.replace('aya' , ' ')
            s = s.replace('ye', ' ')
            s = s.replace('woo' , ' ')
            s = s.replace('ma', ' ')
            
        if not s.strip():
            answer += 1
            
    return answer
'''

def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for s in babbling:
        for word in words:
            if word * 2 in s:
                break
            s = s.replace(word, ' ')
        if not s.strip():
            answer += 1
    return answer
