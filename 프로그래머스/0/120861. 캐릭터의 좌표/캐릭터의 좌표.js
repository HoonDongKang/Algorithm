function solution(keyinput, board) {
  const maximumX = (board[0] - 1) / 2;
  const maximumY = (board[1] - 1) / 2;
  let answer = [0, 0];
  keyinput.forEach((input) => {
    switch (input) {
      case 'left':
        answer[0] =
          Math.abs(answer[0] - 1) > maximumX ? -maximumX : answer[0] - 1;
        break;
      case 'right':
        answer[0] = answer[0] + 1 > maximumX ? maximumX : answer[0] + 1;
        break;
      case 'up':
        answer[1] = answer[1] + 1 > maximumY ? maximumY : answer[1] + 1;
        break;
      case 'down':
        answer[1] =
          Math.abs(answer[1] - 1) > maximumY ? -maximumY : answer[1] - 1;
        console.log(answer[1]);
        break;
    }
  });
  return answer;
}