def solution(n, lost, reserve):
    answer = 0
    result = [0] * (n+2)
    lost.sort()
    reserve.sort()
    for i in range(1, n+1):
        if i not in lost:
            result[i] = 1
    for num in reserve:
        result[num] = 2
        if num in lost:
            result[num] = 1
    for num in lost:
        if result[num-1] == 2:
            result[num] = 1
            result[num-1] = 1
        elif result[num+1] == 2:
            result[num] = 1
            result[num+1] = 1
    answer = len(result) - result.count(0)
    return answer