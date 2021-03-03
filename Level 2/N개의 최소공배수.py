def solution(arr):
    answer = arr[0]
    arr.sort()

    def euclid(n1, n2):
        while n2:
            n1, n2 = n2, n1 % n2
        return n1

    gcd = arr[0]
    for i in arr:
        gcd = euclid(gcd, i)

    for i in arr:
        answer *= (i // gcd)
    return answer


print(solution([2,6,8,14]))