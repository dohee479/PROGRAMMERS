def solution(arr):
    i = arr.index(min(arr))
    arr[i:i+1] = []
    answer = arr
    if not answer:
        answer = [-1]
    return answer

print(solution([4, 3, 2, 1]))