import re


def solution(new_id):
    new_id = new_id.lower()
    p = re.compile('[a-z0-9_.]|-')
    new_id = "".join(p.findall(new_id))
    # 이부분을 정규표현식으로 처리해보자
    new_id = re.sub('[.]+', '.', new_id)
    if new_id[0] == ".":
        new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]
    if not new_id:
        new_id = "a"
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
    return new_id


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
