function solution(num, total) {
  let answer = [];

  const center = Math.floor(total / num);
  if (num % 2 !== 0) {
    const start = (num - 1) / 2;
    answer = Array.from({ length: num }, (_, index) => center - start + index);
  } else {
    const odd = num - 1;
    const start = (odd - 1) / 2;
    answer = Array.from({ length: num }, (_, index) => center - start + index);
  }

  return answer;
}