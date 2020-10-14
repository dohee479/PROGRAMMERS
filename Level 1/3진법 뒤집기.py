def notation(n, num):
    q, r = divmod(n, num)
    if q == 0:
        return str(r)
    return notation(q, num) + str(r)


def solution(n):
    answer = 0
    three = notation(n, 3)
    for i, value in enumerate(three):
        answer += int(value) * (3 ** i)
    return answer


print(solution(45))