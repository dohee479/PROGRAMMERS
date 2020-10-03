def solution(x, n):
    answer = []
    if x < 0:
        x *= -1
        for i in range(x, x * n + 1, x):
            answer.append(-i)
    elif x > 0:
        for i in range(x, x * n + 1, x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)
    return answer

print(solution(2, 5))

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i * x)
    return answer