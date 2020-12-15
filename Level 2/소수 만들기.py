from itertools import combinations


def solution(nums):
    answer = 0

    def prime(sum_comb):
        for j in range(2, int(sum_comb ** 0.5) + 1):
            if not sum_comb % j:
                return 0
        return 1

    comb = list(combinations(nums, 3))
    for i in comb:
        answer += prime(sum(i))

    return answer


print(solution([1, 2, 3, 4]))