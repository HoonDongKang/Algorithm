const getPrimeFactors = (number) => {
  const factors = [];
  let divisor = 2;
  while (number > 1) {
    if (number % divisor === 0) {
      factors.push(divisor);
      number /= divisor;
    } else {
      divisor++;
    }
  }
  return factors;
};

const isFiniteDecimal = (number) => {
  const factors = getPrimeFactors(number);
  return factors.every((factor) => factor === 2 || factor === 5) ? 1 : 2;
};

function solution(a, b) {
  const gcd = (x, y) => (y === 0 ? x : gcd(y, x % y));
  const gcdValue = gcd(a, b);
  b /= gcdValue;

  return isFiniteDecimal(b);
}