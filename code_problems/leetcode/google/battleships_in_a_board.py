def battleships_in_a_board(board: list[list[str]]) -> int:
    cnt = [0]

    def dfs(r, c, isNew):
        if (
            r < 0
            or r >= len(board)
            or c < 0
            or c >= len(board[r])
            or board[r][c] != "X"
        ):
            return
        if isNew:
            cnt[0] += 1
        board[r][c] = "."
        dfs(r + 1, c, False)
        dfs(r - 1, c, False)
        dfs(r, c + 1, False)
        dfs(r, c - 1, False)

    for i in range(len(board)):
        for j in range(len(board[i])):
            dfs(i, j, True)

    return cnt[0]


def test_case(board):
    res = battleships_in_a_board(board)
    print(res)


def main():
    test_case([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])  # 2
    test_case([["."]])  # 0


if __name__ == "__main__":
    main()
