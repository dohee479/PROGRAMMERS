def solution(n):
    if int(n ** 0.5) ** 2 == n:
        answer = int(((n ** 0.5) + 1) ** 2)
    else:
        answer = -1
    return answer


print(solution(121))