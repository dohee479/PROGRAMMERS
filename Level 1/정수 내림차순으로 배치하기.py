def solution(n):
    answer = 0
    number = sorted(str(n), reverse=True)
    for index, num in enumerate(number):
        answer += int(num) * (10 ** (len(number) - index  - 1 ))
    return answer

print(solution(118372))