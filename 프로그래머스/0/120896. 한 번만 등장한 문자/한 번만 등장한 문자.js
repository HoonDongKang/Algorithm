function solution(s) {
  let count = {};

  for (let char of s) {
    count[char] = (count[char] || 0) + 1;
  }

  return Object.keys(count)
    .filter((el) => count[el] === 1)
    .sort()
    .join("");
}