def solution(dartResult):
    answer = 0
    stack = []
    for i in reversed(dartResult):
        if i == 'S':
            if stack[-1] == '*':
                stack.append(1)
        elif i == 'D':
            stack.append(2)
        elif i == 'T':
            stack.append(3)
        elif i == '*':
            stack.append('*')
        elif i == '#':
            stack.append(-1)
        else:
            if '*' in stack:
                stack.append()
            answer += int(i) ** stack.pop()

    return answer


print(solution('1S2D*3T'))