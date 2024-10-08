function solution(n) {
  const countOnes = (num) => num.toString(2).split('1').length - 1;

  const nOnes = countOnes(n);
  let next = n + 1;

  while (countOnes(next) !== nOnes) {
    next++;
  }

  return next;
}
