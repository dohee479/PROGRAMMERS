def solution(arr):
    # 최대 공약수를 구하는 유클리드 호제법
    # A = Bq + R
    # A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
    def gcd(n1, n2):
        while n1:
            n1, n2 = n2 % n1, n1
        return n2

    # 두 수의 최소공배수는 두 수를 곱한후 최대공약수로 나누면 된다.
    # 두개의 최소공배수를 구하고 그 다음 index의 있는 수와의 최소공배수를 구하는 식
    lcm = arr[0]
    for i in arr:
        lcm = (lcm * i) // gcd(lcm, i)

    return lcm


print(solution([2, 3, 4, 5]))