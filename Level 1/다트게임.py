def solution(dartResult):
    answer = 0
    stack = []
    for i in dartResult:
        if i == 'S':
            stack.append(stack.pop() ** 1)
        elif i == 'D':
            stack.append(stack.pop() ** 2)
        elif i == 'T':
            stack.append(stack.pop() ** 3)
        elif i == '*':
            if len(stack) == 1:
                stack.append(stack.pop() * 2)
            else:
                stack.append(stack.pop(-2) * 2)
                stack.append(stack.pop(-2) * 2)
        elif i == '#':
            stack.append(stack.pop() * -1)
        else:
            if i == '0':
                if stack:
                    if stack[-1] == 1:
                        stack.pop()
                        stack.append(10)
                    else:
                        stack.append(0)
                else:
                    stack.append(0)
            else:
                stack.append(int(i))
    for i in stack:
        answer += i

    return answer


print(solution("1D2S#10S"))