def solution(arr1, arr2):
    answer = []
    for i, num1 in enumerate(arr1):
        ls = []
        for j, num2 in enumerate(num1):
            ls.append(num2 + arr2[i][j])
        answer.append(ls)
    return answer


print(solution([[1,2],[2,3]], [[3,4],[5,6]]))