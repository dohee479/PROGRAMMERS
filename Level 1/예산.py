def solution(d, budget):
    answer = 0
    sum_price = 0
    for price in sorted(d):
        if sum_price + price <= budget:
            sum_price += price
            answer += 1
    return answer


print(solution([1,3,2,5,4], 9))