def maps(arr, n):
    global secret
    for i in arr:
        for j, value in enumerate('0' * (n - len(bin(i)[2:]) + str(bin(i)))):
            print(value, end=" ")
        print()


def solution(n, arr1, arr2):
    answer = [''] * n
    global secret
    secret = [[''] * n for _ in range(n)]
    maps(arr1, n)
    maps(arr2, n)
    # for i, value in enumerate(secret):
    #     for j in value:
    #         answer[i] += j
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))