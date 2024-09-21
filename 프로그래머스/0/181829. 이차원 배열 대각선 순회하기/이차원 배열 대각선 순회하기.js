function solution(board, k) {
   let sum = 0;
    const n = board.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < board[i].length; j++) {
            if (i + j <= k) {
                sum += board[i][j];
            }
        }
    }
    
    return sum;
}