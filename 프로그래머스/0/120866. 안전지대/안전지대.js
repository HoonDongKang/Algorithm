function solution(board) {
  const rows = board.length;
  const cols = board[0].length;

  const unsafe = Array.from({ length: rows }, () => Array(cols).fill(false));

  const directions = [
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, -1],
    [0, 1],
    [1, -1],
    [1, 0],
    [1, 1],
  ];

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (board[i][j] === 1) {
        unsafe[i][j] = true;

        for (let [dx, dy] of directions) {
          const x = i + dx;
          const y = j + dy;
          if (x >= 0 && x < rows && y >= 0 && y < cols) {
            unsafe[x][y] = true;
          }
        }
      }
    }
  }
  return unsafe.reduce((count, row) => {
    return count + row.filter((cell) => !cell).length;
  }, 0);
}