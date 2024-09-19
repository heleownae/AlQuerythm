def solution(babbling):
    talk={"aya":'1', "ye":'2', "woo":'3', "ma":'4'}
    dup=['11','22','33','44']
    result=[]
    num=0

    for i in babbling:
        for a,b in talk.items():
            i = i.replace(a,b)  # 옹알이 단어에 대치되는 문자를 숫자로 치환한다.
        result.append(i)

    for i,j in enumerate(result):
        for e in dup:
            if e in j:  # 중복문자가 있을 때는 임의의 문자 'a'로 치환한다. 왜냐하면
                j = j.replace(e,'a')
        if j.isdecimal():  # 숫자만 있는 조건을 필터링하기 때문이다.
            print(j)
            num+=1

    return num
