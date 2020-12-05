def solution(numbers):
    answer = 0
    result = ''

    def backtrack(result):
        cnt = 0
        a = len(result)
        if 1 <= a < len(numbers):
            cnt += 1
            return

        for num in numbers:
            backtrack(result + num)

    backtrack(result)
    return answer


print(solution("17"))
print(solution("011"))