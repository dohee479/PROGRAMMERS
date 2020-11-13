def solution(progresses, speeds):
    answer = []
    stack = []
    for work, speed in zip(progresses, speeds):
        stack.append(round((100 - work) / speed + 0.49))
    print(stack)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))