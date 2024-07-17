def solution(s):
    # join() : 문자열의 메서드로, 리스트나 튜플과 같은 iterable 객체의 각 요소를 하나의 문자열로 합침
    return ''.join(sorted(s, reverse=True))
