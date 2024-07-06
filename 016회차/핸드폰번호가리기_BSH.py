def solution(phone_number):
    import re
    return re.sub(r'\d(?=\d{4})','*',phone_number)
