def solution(arr):
    answer = arr[0]
    arr.sort()

    # 유클리드 호제법 이해하자.
    def euclid(n1, n2):
        while n1:
            n1, n2 = n2 % n1, n1
        return n2

    gcd = arr[0]
    for i in arr:
        gcd = euclid(gcd, i)

    for i in range(1, len(arr)):
        answer *= (arr[i] // gcd)
    return answer


print(solution([3, 7, 10]))