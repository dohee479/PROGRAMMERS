def solution(citations):
    citations.sort(reverse=True)
    for i, value in enumerate(citations):
        if len(citations[:i]) >= value:
            return i
    return len(citations)


print(solution([3, 0, 6, 1, 5]))
print(solution([10,11,12,13]))