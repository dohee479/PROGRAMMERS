def solution(N, stages):
    gamer = len(stages)
    count = [0] * (N + 1)
    fail = {}
    pre_value = 0
    for i in stages:
        if i < N+1:
            count[i] += 1
    for i, value in enumerate(count):
        if i:
            if gamer and value:
                gamer -= pre_value
                fail[i] = value / gamer
                pre_value = value
            else:
                fail[i] = 0
    return sorted(fail, key=lambda x : fail[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))