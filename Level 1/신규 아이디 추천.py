import re


def solution(new_id):
    answer = ''
    special = ["!", "#", "@", "*"]
    new_id = new_id.lower()
    for i in special:
        new_id = new_id.replace(i, "")
    # 이부분을 정규표현식으로 처리해보자
    print(new_id)
    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))