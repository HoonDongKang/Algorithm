function solution(n) {
  let a = 1;
  let b = 2;

  if (n === 1) return a;
  if (n === 2) return b;
  for (let i = 3; i <= n; i++) {
    const temp = (a + b) % 1234567;
    a = b;
    b = temp;
  }

  return b;
}

console.log(solution(4));
