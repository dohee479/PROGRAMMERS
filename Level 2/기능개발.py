def solution(progresses, speeds):
    answer = []
    stack = []
    for work, speed in zip(progresses, speeds):
        stack.append(round((100 - work) / speed + 0.49))
    compare = 0
    cnt = 1
    for i, value in enumerate(stack):
        if i:
            if value <= compare:
                cnt += 1
            else:
                compare = value
                answer.append(cnt)
                cnt = 1
        else:
            compare = value
    answer.append(cnt)
    return answer


def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s) , 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


print(solution([93, 30, 55, 60, 40, 65],  [1, 30, 5 , 10, 60, 7]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]	))