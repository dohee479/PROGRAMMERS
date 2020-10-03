def solution(x):
    answer = True
    original = x
    digit = 0
    while x:
        digit += x % 10
        x //= 10
    if original % digit:
        answer = False
    return answer


print(solution(10))