# 수정 중
from datetime import datetime
from dateutil.relativedelta import relativedelta

today="2022.05.19"
terms=["A 6", "B 12", "C 3"]
privacies=["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

for a,b in enumerate(privacies):
    for t in terms:
        if t[0]==b[11]:
            date_st = b[0:10]
            date_ob = datetime.strptime(date_st, "%Y.%m.%d").date()  # 가입일자 형식변환

            date_to = datetime.strptime(today, "%Y.%m.%d").date()  # 오늘 일자
            date_nw = date_ob + relativedelta(months=int(t[2]))  # 약관 마감일자

            print(date_nw)

            # if date_nw < date_to:
                # print(f'{a+1}번째 인덱스는 약관 기간을 초과했습니다.')
