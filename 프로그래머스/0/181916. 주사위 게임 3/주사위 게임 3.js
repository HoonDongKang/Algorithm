function solution(r, s, e, f) {
  let dice = [r, s, e, f].sort((a, b) => a - b);
  const [a, b, c, d] = dice;

  let count = {};

  dice.forEach((num) => {
    count[num] = (count[num] || 0) + 1;
  });

  const values = Object.keys(count).map(Number);
  const frequencies = Object.values(count);

  if (frequencies.length === 1) return 1111 * a;
  if (frequencies.length === 4) return Math.min(...dice);
  if (frequencies.includes(3)) {
    const x = values.find((v) => count[v] === 3);
    const y = values.find((v) => count[v] === 1);
    return Math.pow(10 * x + y, 2);
  }

  if (frequencies.every((v) => v === 2)) {
    const [x, y] = values;
    return (x + y) * Math.abs(x - y);
  }

  if (frequencies.includes(2) && frequencies.length === 3) {
    const [x, y] = values.filter((v) => count[v] === 1);
    return x * y;
  }

  return 0;
}
