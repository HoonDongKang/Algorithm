function solution(cards1, cards2, goal) {
  let result = 'Yes';

  goal.forEach((card) => {
    if (card === cards1[0]) {
      cards1.shift();
    } else if (card === cards2[0]) {
      cards2.shift();
    } else {
      result = 'No';
      return;
    }
  });
  return result;
}