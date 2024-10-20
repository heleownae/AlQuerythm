def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split('.'))

    term_dict = {}
    for term in terms:
        kind, validity = term.split()
        term_dict[kind] = int(validity)
    
    to_delete = []
    
    for i, privacy in enumerate(privacies):
        date, kind = privacy.split()
        year, month, day = map(int, date.split('.'))
        
        validity_months = term_dict[kind]

        expire_month = month + validity_months
        expire_year = year + (expire_month - 1) // 12
        expire_month = (expire_month - 1) % 12 + 1

        if (expire_year < today_year) or (expire_year == today_year and expire_month < today_month) or (expire_year == today_year and expire_month == today_month and day <= today_day):
            to_delete.append(i + 1)  # 1-based index

    return to_delete
