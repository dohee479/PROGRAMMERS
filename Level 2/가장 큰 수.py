# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers = sorted(numbers, key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))


import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

def myQuickSort(nums, l, r):
    if l >= r:
        return

    # pos를 진행하면서 l에서 r까지의 범위가 정렬이 됨 (우선순위 가장 작은게 맨 뒤로 감)
    # pos는 nums에서 가장 우선순위가 작은 값
    pos = partition(nums, l, r)

    # QuickSort는 pos(우선선위가 가장 작은 값)
    myQuickSort(nums, l, pos-1)
    myQuickSort(nums, pos+1, r)

def partition(nums, l, r):
    # print(nums, l, r)
    low = l
    while l < r:
        # l + r > r + l 이면
        if compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1

        l += 1

    # 가장 낮은 순위 low를 가장 오른쪽 r과 변경
    # 여기서 r은 분할정복으로 들어왔기에 들어온 값중에서 마지막임
    nums[low], nums[r] = nums[r], nums[low]
    return low

def compare(n1, n2):
    return str(n1) + str(n2) > str(n2) + str(n1)

def solution(numbers):
    myQuickSort(numbers, 0, len(numbers)-1)
    answer = str(int("".join(map(str, numbers))))
    return answer
