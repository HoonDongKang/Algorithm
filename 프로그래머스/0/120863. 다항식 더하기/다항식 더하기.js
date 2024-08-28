function solution(polynomial) {
  const values = polynomial.split(' + ');

  const xSum = values
    .filter((value) => value.includes('x'))
    .map((value) => value.replace('x', '') || '1')
    .reduce((acc, cur) => acc + Number(cur), 0);

  const numSum = values
    .filter((value) => !value.includes('x'))
    .reduce((acc, cur) => acc + Number(cur), 0);

  let answer = '';
  if (xSum) {
    if (xSum === 1) {
      answer += 'x';
    } else {
      answer += `${xSum}x`;
    }
  }

  if (xSum && numSum) answer += ' + ';
  if (numSum) answer += `${numSum}`;
  return answer;
}