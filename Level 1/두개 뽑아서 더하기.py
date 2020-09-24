def backtrack(numbers, index, cnt, m, result):
    global visited
    if cnt == m:
        answer.add(result)
        return

    for i in range(index, len(numbers)):
        if visited[i]:
            continue
        for j in range(i + 1):
            visited[j] = 1
        backtrack(numbers, i + 1, cnt + 1, m, result + numbers[i])
        for j in range(len(numbers)):
            visited[j] = 0


def solution(numbers):
    global answer, visited
    answer = set()
    visited = [0] * len(numbers)
    backtrack(numbers, 0, 0, 2, 0)
    return sorted(list(answer))


print(solution(([2,1,3,4,1])))