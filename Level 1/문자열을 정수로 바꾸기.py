def solution(s):
    # if s[0] == '+':
    #     answer = int(s[1:])
    # elif s[0] == '-':
    #     answer = -int(s[1:])
    # else:
    #     answer = int(s)
    answer = int(s)
    return answer

print(solution('-1234'))

def solution(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result