def solution(s):
    answer = []
    words = s.split()
    # 띄어쓰기 기준으로 자른 단어 대소문자 변경
    for word in words:
        new_word = ''
        for i, j in enumerate(word):
            if i % 2 == 0:  
                new_word += j.upper()
            else: 
                new_word += j.lower()
                # 대소문자 바꾼거 저장
        answer.append(new_word) 
    return ' '.join(answer)
# 틀림????

def solution(s):
    answer = [] 
    # 단어를 공백으로 나누되, 공백도 유지하기 위해 split() 대신 split(' ') 사용
    words = s.split(' ')    
    for word in words:
        new_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0: 
                new_word += char.upper()
            else:
                new_word += char.lower()
        answer.append(new_word)  
    return ' '.join(answer)
