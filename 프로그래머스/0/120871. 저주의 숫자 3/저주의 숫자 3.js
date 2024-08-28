const isBad = (num) => {
  if (num % 3 === 0) return true;
  if ([...(num + '')].includes('3')) return true;
  else return false;
};

function solution(n) {
  let count = 0;
  for (let i = 0; i < n; i++) {
    count++;
    while (isBad(count)) {
      count++;
    }
  }

  return count;
}
