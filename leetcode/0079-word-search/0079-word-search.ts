function exist(board: string[][], word: string): boolean {
    const rows = board.length;
    const cols = board[0].length;

    function dfs(i: number, j: number, k: number): boolean {
        if (k === word.length) return true;

        if (i < 0 || j < 0) return false;
        if (i >= rows || j >= cols) return false;
        if (board[i][j] !== word[k]) return false;

        const temp = board[i][j];
        board[i][j] = "#";

        const result =
            dfs(i + 1, j, k + 1) ||
            dfs(i - 1, j, k + 1) ||
            dfs(i, j + 1, k + 1) ||
            dfs(i, j - 1, k + 1);

        board[i][j] = temp;
        return result;
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (dfs(i, j, 0)) return true;
        }
    }

    return false;
};