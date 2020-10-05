def solution(N, stages):
    gamer = len(stages)
    count = [0] * (N + 1)
    fail = [0] * (N + 1)
    for i in stages:
        if i <= N:
            count[i] += 1
    for i, value in enumerate(count):
        if i and value:
            gamer -= count[i - 1]
            fail[i] = value / gamer
    answer = sorted(range(1, N+1), key=lambda x: fail[x], reverse=True)
    return answer

print(solution(8, [1,2,3,4,5,6,7]))