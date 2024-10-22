def solution(today, terms, privacies):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    result=[]

    for a,b in enumerate(privacies):
        for t in terms:
            if t[0]==b[11]:
                date_st = b[0:10]
                date_jo = datetime.strptime(date_st, "%Y.%m.%d").date()  # 가입일자 형식변환
                date_in = date_jo - relativedelta(days=1)

                date_to = datetime.strptime(today, "%Y.%m.%d").date()  # 오늘 일자
                date_nw = date_in + relativedelta(months=int(t[2:]))  # 약관 마감일자

                print(date_nw)

                if date_nw < date_to:
                    result.append(a+1)

    return result
