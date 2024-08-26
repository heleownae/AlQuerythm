def solution(a, b):
    
    #2016년은 윤년!
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    total = sum(month[:a-1]) + b - 1
    answer = week[total % 7]
    
    return answer
