function solution(arr) {
  let min = 1;
  while (min < arr.length) {
    min *= 2;
  }

  if (min === arr.length) return arr;
  else {
    return [...arr, ...Array.from({ length: min - arr.length }).fill(0)];
  }
}
