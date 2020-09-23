def solution(arr, divisor):
    answer = []
    arr.sort()
    for i in range(len(arr)):
        if not arr[i] % divisor:
            answer.append(arr[i])
    if len(answer) == 0:
        answer.append(-1)
    return answer