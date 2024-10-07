function solution(n) {
  let count = 0;

  for (let m = 0; (m * (m + 1)) / 2 < n; m++) {
    if ((n - (m * (m + 1)) / 2) % (m + 1) === 0) {
      count++;
    }
  }

  return count;
}