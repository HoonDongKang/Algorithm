function solution(i, j, k) {
  const arr = Array.from({ length: j - i + 1 }, (_, start) => start + i);
  let count = 0;
  for (let number of arr) {
    if ([...(number + '')].filter((el) => el === k + '').length) {
      count += [...(number + '')].filter((el) => el === k + '').length;
    }
  }
  return count;
}