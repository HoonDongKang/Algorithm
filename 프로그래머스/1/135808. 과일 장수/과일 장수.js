function solution(k, m, score) {
  const scores = score.sort((a, b) => b - a);
  let result = [];
  let arr = [];
  scores.forEach((value, i) => {
    if ((i + 1) % m !== 0) {
      arr.push(value);
    } else {
      result.push([...arr, value]);
      arr = [];
    }
  });
  return result.reduce((acc, cur) => acc + Math.min(...cur) * m, 0);
}