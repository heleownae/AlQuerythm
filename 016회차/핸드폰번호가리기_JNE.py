def solution(phone_number):
# 첫문자~-5번 문자까지 * 로 대체
# *에 대체할 문자 갯수를 곱해서 출력
    return phone_number.replace(phone_number[0:-4], '*' * len(phone_number[0:-4]))
