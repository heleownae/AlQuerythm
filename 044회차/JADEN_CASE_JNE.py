def solution(s):
    words = s.split(' ')
    jaden = []
    for word in words:
        if word: 
            chg = word[0].upper() + word[1:].lower()
            jaden.append(chg)
        else:
            jaden.append('')
    
    return ' '.join(jaden)
