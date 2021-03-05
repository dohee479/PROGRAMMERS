# 유클리드 호제법을 이용하여 풀려했으나 실패
def solution(arr):
    answer = 1
    for i in range(len(arr)):
        num = arr[i]
        for j in range(i, len(arr)):
            if not (arr[j] % num):
                arr[j] = arr[j] // num
        answer *= num
    return answer


print(solution([3,4,9,16]))