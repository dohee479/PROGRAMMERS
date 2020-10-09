def maps(arr):
    global secret
    for i, value in enumerate(arr):
        for j, b in enumerate(bin(value)):
            if j > 1:
                if b == '1':
                    secret[i][j - 1] = '#'
                else:
                    secret[i][j - 1] = ' '

def solution(n, arr1, arr2):
    answer = [''] * n
    global secret
    secret = [[''] * n for _ in range(n)]
    maps(arr1)
    maps(arr2)
    print(secret)
    # for i, value in enumerate(secret):
    #     for j in value:
    #         answer[i] += j
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))