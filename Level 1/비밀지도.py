def maps(arr, n):
    global secret
    for i, num in enumerate(arr):
        for j, value in enumerate(('0' * (n - len(bin(num)[2:])) + bin(num)[2:])):
            if value == "0":
                if secret[i][j] == "#":
                    continue
                secret[i][j] = ' '
            else:
                secret[i][j] = '#'


def solution(n, arr1, arr2):
    answer = [''] * n
    global secret
    secret = [[''] * n for _ in range(n)]
    maps(arr1, n)
    maps(arr2, n)
    for i, value in enumerate(secret):
        for j in value:
            answer[i] += j
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer