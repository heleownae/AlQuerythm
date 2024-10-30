def solution(id_list, report, k):
    report_dict = {user: set() for user in id_list}
    
    for r in report:
        reporter, reported = r.split()
        report_dict[reporter].add(reported)
    
    report_count = {user: 0 for user in id_list}
    for reporters in report_dict.values():
        for reported in reporters:
            report_count[reported] += 1
    
    suspended_users = {user for user, count in report_count.items() if count >= k}
    
    mail_count = [0] * len(id_list)
    for i, user in enumerate(id_list):
        for reported in report_dict[user]:
            if reported in suspended_users:
                mail_count[i] += 1
    
    return mail_count
