def solution(arr):
    ans = []
    ans.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != ans[-1]:
            ans.append(arr[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    return ans