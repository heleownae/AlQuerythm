import pandas as pd
def solution(a, b):
    temp = f'2016-{a}-{b}'
    date = pd.to_datetime(temp).day_name()  # 기준 날짜 설정. dt.~는 시리즈나 데이터프레임에 사용
    return date.upper()[:3]
