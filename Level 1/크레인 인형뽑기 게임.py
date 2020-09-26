def solution(board, moves):
    answer = 0
    basket = []
    for index, move in enumerate(moves):
        visited = [True] * len(moves)
        for i, k in enumerate(board):
            for j, doll in enumerate(k):
                if j == move - 1 and doll and visited[index]:
                    if basket:
                        if basket[-1] == doll:
                            basket.pop()
                            board[i][j] = 0
                            visited[index] = False
                            answer += 2
                        else:
                            basket.append(doll)
                            board[i][j] = 0
                            visited[index] = False
                    else:
                        basket.append(doll)
                        board[i][j] = 0
                        visited[index] = False
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))