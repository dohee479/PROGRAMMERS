import re


def solution(s):
    answer = [0, 0]

    def binary(n):
        binary_num = ''
        while n:
            n, r = divmod(n, 2)
            binary_num += str(r)
        return binary_num[::-1]

    while s != "1":
        s_len = len(s)
        s = re.sub("0", "", s)
        answer[1] += s_len - len(s)
        s = binary(len(s))
        answer[0] += 1
    return answer


print(solution("110010101001"))